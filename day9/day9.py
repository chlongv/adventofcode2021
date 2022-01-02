import argparse
import numpy as np
import pathlib
import typing


def read_input(file: pathlib.Path) -> np.ndarray:
    with open(file) as f:
        lines = f.readlines()
        nb_lines = len(lines)
        values = []
        for l in lines:            
            values.extend([int(c) for c in l.replace('\n','')])
        nb_elem = len(values) // nb_lines
        depth_map = np.array(values, dtype=np.int8).reshape((nb_lines, nb_elem))
        return depth_map


def find_low(map: np.ndarray, debug: bool) -> np.ndarray:
    low_map = np.full(map.shape, -1)
    dims = map.shape
    for index, v in np.ndenumerate(map):
        neighbors = [127, 127, 127, 127]
        # find the real neighbor when possible (i.e. not on a border)
        if index[0] > 0:
            neighbors[0] = map[index[0]-1][index[1]]
        if index[0] < dims[0] - 1:
            neighbors[1] = map[index[0]+1][index[1]]
        if index[1] > 0:
            neighbors[2] = map[index[0]][index[1]-1]
        if index[1] < dims[1] - 1:
            neighbors[3] = map[index[0]][index[1]+1]
        
        # if we're lower than all neibors, we have a low
        if all(v < n for n in neighbors):
            # we have a low
            low_map[index[0]][index[1]] = v
    if debug:
        print(low_map)
    return low_map


def compute_risk(map: np.ndarray) -> int:
    risk = 0
    for _, v in np.ndenumerate(map):
        if v != -1:
            risk += v + 1
    return risk


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Solve day9 exercise')
    parser.add_argument('file', type=pathlib.Path, help='input file')
    parser.add_argument('-d', '--debug', action='store_true', help='debug')

    args = parser.parse_args()

    depth_map = read_input(args.file)
    low_map = find_low(depth_map, args.debug)
    print(compute_risk(low_map))
    