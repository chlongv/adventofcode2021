import argparse
import numpy as np
import pathlib

from numpy.core.fromnumeric import shape

def read_input(file: pathlib.Path) -> np.array:
    with open(file) as f:
        lines = f.readlines()
    
    vents = []
    for l in lines:
        vent = [int(vent) for vent in l.replace(' -> ', ',').split(',')]
        vent = np.array(vent).reshape(2,2)
        vents.append(vent)
    
    return vents

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Solve day5 exercise')
    parser.add_argument('file', type=pathlib.Path, help='input file')

    args = parser.parse_args()

    vents = read_input(args.file)