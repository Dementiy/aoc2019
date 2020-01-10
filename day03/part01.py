import sys

from functools import partial
from typing import List, NamedTuple, Tuple


class Point(NamedTuple):
    x: int
    y: int


DIRECTIONS = {
    "R": Point(1, 0),
    "L": Point(-1, 0),
    "U": Point(0, 1),
    "D": Point(0, -1),
}


def read_wires(filename: str) -> Tuple[List[str], List[str]]:
    with open(filename) as f:
        wire1, wire2 = map(str.strip, f.readlines())
    return wire1.split(","), wire2.split(",")


def manhattan(p: Point, q: Point) -> int:
    """
    >>> manhattan(Point(1,1), Point(5,4))
    7
    """
    return sum(abs(pi - qi) for pi, qi in zip(p, q))


def trace_wire(wire: List[str]) -> List[Point]:
    trace = []
    p = Point(0, 0)
    steps = ((v[0], int(v[1:])) for v in wire)
    for d, step_size in steps:
        for _ in range(step_size):
            move_to = DIRECTIONS[d]
            p = Point(p.x + move_to.x, p.y + move_to.y)
            trace.append(p)
    return trace


def closest_distance(w1: List[str], w2: List[str]) -> int:
    """
    >>> closest_distance(
    ... ['R75', 'D30', 'R83', 'U83', 'L12', 'D49', 'R71', 'U7', 'L72'],
    ... ['U62', 'R66', 'U55', 'R34', 'D71', 'R55', 'D58', 'R83']
    ... )
    159
    >>> closest_distance(
    ... ['R98', 'U47', 'R26', 'D63', 'R33', 'U87', 'L62', 'D20', 'R33', 'U53', 'R51'],
    ... ['U98', 'R91', 'D20', 'R16', 'D67', 'R40', 'U7', 'R15', 'U6', 'R7']
    ... )
    135
    """
    distance = partial(manhattan, Point(0, 0))
    return sum(min(set(trace_wire(w1)) & set(trace_wire(w2)), key=distance))


if __name__ == "__main__":
    w1, w2 = read_wires(sys.argv[1])
    print(closest_distance(w1, w2))
