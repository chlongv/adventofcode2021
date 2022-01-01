import argparse
import pathlib
import sys
import typing


def read_input(file:pathlib.Path) -> typing.Dict:
    with open(file) as f:
        lfs = f.readline()
        crab_positions = [int(lf) for lf in lfs.split(',')]
        return crab_positions

def cost_part2(n: int) -> int:
    return n * (n + 1) // 2

def fuel_cost(pos: typing.List, goal_pos: int, f: typing.Callable[[int], int]) -> int:
    return sum([f(abs(p-goal_pos)) for p in pos])


def find_lowest_fuel_cost(initial_positions: typing.List) -> int:
    max_pos = max(initial_positions)
    min_fuel_cost, optimal_pos = sys.maxsize, 0
    for pos in range(0, max_pos):
        # cost = fuel_cost(initial_positions, pos, lambda x: x)
        cost = fuel_cost(initial_positions, pos, cost_part2)
        if cost <= min_fuel_cost:
            min_fuel_cost = cost
            optimal_pos = pos
    return min_fuel_cost, optimal_pos


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Solve day6 exercise')
    parser.add_argument('file', type=pathlib.Path, help='input file')
    parser.add_argument('-d', '--debug', action='store_true', help='debug')

    args = parser.parse_args()

    crab_positions = read_input(args.file)
    opt_fuel, optimal_pos = find_lowest_fuel_cost(crab_positions)
    print(f'{opt_fuel=} {optimal_pos=}')
