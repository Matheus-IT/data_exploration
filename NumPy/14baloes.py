from dataclasses import dataclass
from typing import List, Union


@dataclass
class Dot:
    x: int
    y: int


@dataclass
class Segment:
    start: Dot
    end: Dot
    segment_tilt_direction: Union[Dot, None]

    def this_balloon_is_gonna_hit(self, balloon: Dot):
        return self.start.x <= balloon.x <= self.end.x


# Utils ---------------------------------------------------------------
def read_numbers():
    try:
        input_data = input()
    except EOFError:
        return []
    return list(map(int, input_data.split(' ')))


def segment_tilt_direction(x1, y1, x2, y2):
    if not y1 != y2:
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
    tilted_segments: List[Segment] = []
    flat_segments: List[Segment] = []

    for i in range(line_segments):
        x1, y1, x2, y2 = read_numbers()

        segment = Segment(
            start=Dot(x1, y1),
            end=Dot(x2, y2),
            segment_tilt_direction=segment_tilt_direction(x1, y1, x2, y2),
        )

        all_segments.append(segment)

        if segment.segment_tilt_direction:
            tilted_segments.append(segment)
        else:
            flat_segments.append(segment)

    for i in range(queries):
        balloon_x = read_numbers()[0]
        balloon = Dot(x=balloon_x, y=0)

        for segment in tilted_segments:
            if segment.this_balloon_is_gonna_hit(balloon):
                balloon.x = segment.segment_tilt_direction.x
                balloon.y = segment.segment_tilt_direction.y

        for segment in flat_segments:
            if segment.this_balloon_is_gonna_hit(balloon):
                balloon.y = segment.end.y
                print(balloon.x, balloon.y)
            else:
                print(balloon.x)

        if len(flat_segments) == 0:
            print(balloon.x)
