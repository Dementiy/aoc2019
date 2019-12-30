import sys
import math


def get_total_fuel(path: str) -> float:
    with open(path) as f:
        return sum(math.floor(int(mass) / 3) - 2 for mass in f)


if __name__ == '__main__':
    print(get_total_fuel(sys.argv[1]))
