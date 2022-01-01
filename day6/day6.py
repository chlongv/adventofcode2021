import argparse
import pathlib
import typing


def read_input(file:pathlib.Path) -> typing.Dict:
    with open(file) as f:
        lfs = f.readline()
        lanternfishes = [int(lf) for lf in lfs.split(',')]
        population = {k:0 for k in range(0,9)}
        for lf in lanternfishes:
            population[lf] += 1
        return population


def total_pop(pop: typing.Dict) -> int:
    sum = 0
    for _, v in pop.items():
        sum += v
    return sum

def epoch(pop: typing.Dict) -> typing.Dict:
    output = {k:0 for k in range(0,9)}
    for k, v in pop.items():
        if k == 0:
            output[8] += v
            output[6] += v
        else:
            output[k-1] += v
    return output


def count_fishes(initial_pop: typing.Dict, epochs: int, debug: bool) -> int:
    pop = initial_pop
    for i in range(0, epochs):
        pop = epoch(pop)
        if debug:
            print(f'epoch {i}: {total_pop(pop)} fishes: {pop}')
    return total_pop(pop)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Solve day6 exercise')
    parser.add_argument('file', type=pathlib.Path, help='input file')
    parser.add_argument('epochs', type=int, help='number of epochs')
    parser.add_argument('-d', '--debug', action='store_true', help='debug print epochs')

    args = parser.parse_args()

    lf_population = read_input(args.file)
    print(count_fishes(lf_population, args.epochs, args.debug))
