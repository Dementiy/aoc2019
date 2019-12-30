import operator
import sys

from typing import List

OP = {
    1: operator.add,
    2: operator.mul,
}
HALT = 99


def execute(intcode: List[int]) -> List[int]:
    """
    >>> execute([1,9,10,3,2,3,11,0,99,30,40,50])
    [3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50]
    >>> execute([1,0,0,0,99])
    [2, 0, 0, 0, 99]
    >>> execute([2,3,0,3,99])
    [2, 3, 0, 6, 99]
    >>> execute([2,4,4,5,99,0])
    [2, 4, 4, 5, 99, 9801]
    >>> execute([1,1,1,4,99,5,6,0,99])
    [30, 1, 1, 4, 2, 5, 6, 0, 99]
    """
    if not intcode:
        return []

    i = 0
    while True:
        opcode = intcode[i]
        if opcode == HALT:
            return intcode
        pos1, pos2, pos3 = intcode[i+1:i+4]
        intcode[pos3] = OP[opcode](intcode[pos1], intcode[pos2])
        i += 4
    return intcode


def read_intcode(path: str) -> List[int]:
    with open(path) as f:
        return list(map(int, f.read().split(',')))


if __name__ == '__main__':
    intcode = read_intcode(sys.argv[1])
    intcode[1] = 12
    intcode[2] = 2
    print(execute(intcode))
