import argparse
import numpy as np
import pathlib
import typing

from numpy.core.fromnumeric import shape

class Point(typing.NamedTuple):
    x: int
    y: int

class Vent(typing.NamedTuple):
    s: Point
    e: Point


def read_input(file: pathlib.Path) -> typing.List:
    with open(file) as f:
        lines = f.readlines()
    
    vents = []
    for l in lines:
        vent = [int(vent) for vent in l.replace(' -> ', ',').split(',')]
        vent = Vent(Point(vent[0], vent[1]), Point(vent[2], vent[3]))
        vents.append(vent)
    
    return vents


def find_dims(vents: typing.List) -> np.array:
    dims = np.zeros(2, dtype=int)
    for v in vents:
        max_x = max(v.s.x, v.e.x)
        max_y = max(v.s.y, v.e.y)
        dims[0] = np.maximum(max_x, dims[0])
        dims[1] = np.maximum(max_y, dims[1])
    dims += 1
    return dims


def is_horizontal(v: Vent) -> bool:
    return v.s.y == v.e.y


def is_vertical(v: Vent) -> bool:
    return v.s.x == v.e.x


def update_horizontal(map: np.array, v: Vent) -> None:
    y = v.s.y
    x_s, x_e = 0, 0
    if v.s.x < v.e.x:
        x_s, x_e = v.s.x, v.e.x
    else:
        x_s, x_e = v.e.x, v.s.x
    for x in range(x_s, x_e + 1):
        map[x][y] += 1


def update_vertical(map: np.array, v: Vent) -> None:
    x = v.s.x
    y_s, y_e = 0, 0
    if v.s.y < v.e.y:
        y_s, y_e = v.s.y, v.e.y
    else:
        y_s, y_e = v.e.y, v.s.y
    for y in range(y_s, y_e + 1):
        map[x][y] += 1 


def check_vents(vents: np.array) -> int:
    dims = find_dims(vents)
    cloud_map = np.zeros(dims, dtype=int)
    for v in vents:
        if is_horizontal(v):
            update_horizontal(cloud_map, v)
        elif is_vertical(v):
            update_vertical(cloud_map, v)
    return np.count_nonzero(cloud_map > 1)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Solve day5 exercise')
    parser.add_argument('file', type=pathlib.Path, help='input file')

    args = parser.parse_args()

    vents = read_input(args.file)
    dangerous_points = check_vents(vents)
    print(dangerous_points)