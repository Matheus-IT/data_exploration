from dataclasses import dataclass
from typing import List, Union


@dataclass
class Dot:
    x: int
    y: int


@dataclass
class Balloon(Dot):
    is_stuck: bool = False
    flew_away: bool = False


@dataclass
class Segment:
    start: Dot
    end: Dot
    segment_tilt_direction: Union[Dot, None]

    def this_balloon_is_gonna_hit(self, balloon: Balloon):
        if self.segment_tilt_direction is None:
            # In case of a flat segment
            return self.start.x <= balloon.x <= self.end.x and self.start.y > balloon.y
        # In case of a tilted segment
        return self.start.x <= balloon.x <= self.end.x and self.segment_tilt_direction.y > balloon.y


# Utils ---------------------------------------------------------------
def read_numbers():
    try:
        input_data = input()
    except EOFError:
        return []
    return list(map(int, input_data.split(' ')))


def segment_tilt_direction(x1, y1, x2, y2):
    if y1 == y2:
        return None
    if y1 > y2:
        return Dot(x1, y1)
    return Dot(x2, y2)


# ---------------------------------------------------------------------


while True:
    input_data = read_numbers()
    if not input_data:
        break
    line_segments, queries = input_data

    all_segments: List[Segment] = []

    for i in range(line_segments):
        x1, y1, x2, y2 = read_numbers()

        if x2 > x1:
            segment = Segment(
                start=Dot(x1, y1),
                end=Dot(x2, y2),
                segment_tilt_direction=segment_tilt_direction(x1, y1, x2, y2),
            )
        else:
            segment = Segment(
                start=Dot(x2, y2),
                end=Dot(x1, y1),
                segment_tilt_direction=segment_tilt_direction(x1, y1, x2, y2),
            )

        all_segments.append(segment)

    for i in range(queries):
        balloon_x = read_numbers()[0]
        balloon = Balloon(x=balloon_x, y=0)

        segments_balloon_may_hit: List[Segment] = []

        for segment in all_segments:
            if segment.this_balloon_is_gonna_hit(balloon):
                segments_balloon_may_hit.append(segment)

        segments_balloon_may_hit = sorted(segments_balloon_may_hit, key=lambda s: s.start.y)
        segments_balloon_may_hit = sorted(segments_balloon_may_hit, key=lambda s: s.end.y)

        for segment in segments_balloon_may_hit:
            if segment.this_balloon_is_gonna_hit(balloon):
                if segment.segment_tilt_direction is None:
                    # Case of flat segments
                    balloon.y = segment.end.y
                    balloon.is_stuck = True
                    print(balloon.x, balloon.y)
                else:
                    # Case of tilted segments
                    balloon.x = segment.segment_tilt_direction.x
                    balloon.y = segment.segment_tilt_direction.y

        if not balloon.is_stuck:
            balloon.flew_away = True
            print(balloon.x)
