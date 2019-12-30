import itertools
import sys

from typing import List, Optional, Tuple

from part01 import execute, read_intcode


def find_noun_and_verb(intcode: List[int], target: int) -> Optional[Tuple[int, int]]:
    for noun, verb in itertools.product(range(1, 100), range(1, 100)):
        intcode[1] = noun
        intcode[2] = verb
        output, *_ = execute(intcode)
        if output == target:
            return noun, verb
    return None


if __name__ == '__main__':
    target = 19690720
    intcode = read_intcode(sys.argv[1])
    noun, verb = find_noun_and_verb(intcode, target)  # type: ignore
    print(100 * noun + verb)
