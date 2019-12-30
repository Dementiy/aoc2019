import sys
import math


def get_required_fuel(mass: int) -> int:
    """
    >>> get_required_fuel(14)
    2
    >>> get_required_fuel(1969)
    966
    >>> get_required_fuel(100756)
    50346
    """
    fuel = math.floor(mass / 3) - 2
    if fuel <= 0:
        return 0
    else:
        return fuel + get_required_fuel(fuel)


def get_total_fuel(path: str) -> int:
    with open(path) as f:
        return sum(get_required_fuel(int(mass)) for mass in f)


if __name__ == '__main__':
    print(get_total_fuel(sys.argv[1]))
