import argparse
import pathlib
import typing


def read_input(file: pathlib.Path) -> typing.Tuple:
    signals = []
    outputs = []
    with open(file) as f:
        lines = f.readlines()
        for l in lines:
            sep_line = l.split('|')
            signals.append(sep_line[0].split())
            outputs.append(sep_line[1].split())
        return (signals, outputs)


def find_unique_segments(input: typing.List) -> int:
    num = 0
    for line in input:
        for value in line:
            l = len(value)
            if l == 2 or l == 3 or l == 4 or l == 7:
                num += 1
    return num


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Solve day8 exercise')
    parser.add_argument('file', type=pathlib.Path, help='input file')
    parser.add_argument('-d', '--debug', action='store_true', help='debug')

    args = parser.parse_args()

    signals, outputs = read_input(args.file)
    print(find_unique_segments(outputs))