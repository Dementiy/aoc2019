import sys
from typing import List

from part01 import Point, read_wires, trace_wire


def steps(trace: List[Point], p: Point) -> int:
    return trace.index(p) + 1


def optimal_steps(wire1: List[str], wire2: List[str]) -> int:
    """
    >>> optimal_steps(
    ... ['R75', 'D30', 'R83', 'U83', 'L12', 'D49', 'R71', 'U7', 'L72'],
    ... ['U62', 'R66', 'U55', 'R34', 'D71', 'R55', 'D58', 'R83']
    ... )
    610
    >>> optimal_steps(
    ... ['R98', 'U47', 'R26', 'D63', 'R33', 'U87', 'L62', 'D20', 'R33', 'U53', 'R51'],
    ... ['U98', 'R91', 'D20', 'R16', 'D67', 'R40', 'U7', 'R15', 'U6', 'R7']
    ... )
    410
    >>> optimal_steps(
    ... ['R8', 'U5', 'L5', 'D3'],
    ... ['U7', 'R6', 'D4', 'L4']
    ... )
    30
    """
    t1, t2 = trace_wire(wire1), trace_wire(wire2)
    return min(steps(t1, p) + steps(t2, p) for p in set(t1) & set(t2))


if __name__ == "__main__":
    w1, w2 = read_wires(sys.argv[1])
    print(optimal_steps(w1, w2))
