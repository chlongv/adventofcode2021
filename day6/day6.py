import argparse
import copy
import pathlib
import typing


def read_input(file:pathlib.Path) -> typing.List:
    with open(file) as f:
        lfs = f.readline()
        lanternfishes = [int(lf) for lf in lfs.split(',')]
        return lanternfishes


def epoch(input: typing.List) -> typing.List:
    new_fishes = []
    for i, f in enumerate(input):
        if f == 0:
            new_fishes.append(8)
            input[i] = 6
        else:
            input[i] = f - 1
    input.extend(new_fishes)
    return input


def count_fishes(lfs: typing.List, epochs: int, debug: bool) -> int:
    fishes = lfs
    for i in range(0, epochs):
        fishes = epoch(fishes)
        if debug:
            print(f'epoch {i}: {len(fishes)} fishes: {fishes}')
    return len(fishes)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Solve day6 exercise')
    parser.add_argument('file', type=pathlib.Path, help='input file')
    parser.add_argument('epochs', type=int, help='number of epochs')
    parser.add_argument('-d', '--debug', action='store_true', help='debug print epochs')

    args = parser.parse_args()

    lanternfishes = read_input(args.file)
    print(count_fishes(lanternfishes, args.epochs, args.debug))