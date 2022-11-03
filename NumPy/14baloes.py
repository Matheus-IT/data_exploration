import sys
from dataclasses import dataclass
from typing import Union


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
def read_numbers(input_data: str):
    return list(map(int, input_data.split(' ')))


def segment_tilt_direction(x1, y1, x2, y2):
    if y1 == y2:
        return None
    if y1 > y2:
        return Dot(x1, y1)
    return Dot(x2, y2)


# ---------------------------------------------------------------------


for line in sys.stdin:
    input_data = str(line)
    if not input_data:
        break
    line_segments, queries = read_numbers(input_data)

    all_segments = []

    for _ in range(line_segments):
        line = sys.stdin.readline()
        input_data = str(line)
        x1, y1, x2, y2 = read_numbers(input_data)

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

    # Then we sort the segments by the y axis, to put the ones that are
    # closer to the balloon to the beginning of the list
    all_segments = sorted(all_segments, key=lambda s: s.start.y)
    all_segments = sorted(all_segments, key=lambda s: s.end.y)

    for _ in range(queries):
        line = line = sys.stdin.readline()
        input_data = str(line)
        balloon_x = read_numbers(input_data)[0]
        balloon = Balloon(x=balloon_x, y=0)

        # Now that we have the segments in ascending order we can determine if
        # the balloon got stuck or flew away
        for segment in all_segments:
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

        # If the balloon didn't get stuck after checking all flat segments it
        # may hit, we can assure it flew away
        if not balloon.is_stuck:
            balloon.flew_away = True
            print(balloon.x)
