import argparse
import pathlib
import sys
import typing

from collections import deque

def read_depths(depth_file: pathlib.Path) -> typing.List:
    with open(depth_file) as depth_file:
        depths = depth_file.readlines()

    return [int(d.replace('\n','')) for d in depths]

def solve(depths) -> int:
    previous_depth, nb_increased = sys.maxsize, 0
    for depth in depths:
        if depth >= previous_depth:
            nb_increased += 1
        previous_depth = depth

    return nb_increased

def add_elem(q: deque, e: int) -> None:
    q.popleft()
    q.append(e)

def solve_sliding(depths) -> int:
    slice, previous_slice = deque(depths[0:3]), deque(depths[0:3])
    nb_increased = 0
    del depths[0:3]
    depths = deque(depths)
    while depths:
        n = depths.popleft()
        add_elem(slice, n)
        if sum(slice) > sum(previous_slice):
            nb_increased += 1
        add_elem(previous_slice, n)

    return nb_increased


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Solve day1 exercise')
    parser.add_argument('depth_file', type=pathlib.Path, help='depth input file')

    args = parser.parse_args()

    depths = read_depths(args.depth_file)
    print(solve(depths))
    print(solve_sliding(depths))
