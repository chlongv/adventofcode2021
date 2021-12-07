import argparse
import pathlib
import typing

def read_report(file: pathlib.Path) -> typing.List:
    with open(file) as f:
        binaries = f.readlines()

    # get all chars
    binaries = [[c for c in b.replace('\n', '')] for b in binaries]
    transpose = []
    for j, _ in enumerate(binaries[0]):
        col = []
        for l in binaries:
            col.append(l[j])
        transpose.append(col)
    return transpose

def solve(inputs) -> int:
    gamma_bits = []
    for col in inputs:
        ones, zeros = col.count('1'), col.count('0')
        if ones > zeros:
            gamma_bits.append('1')
        else:
            gamma_bits.append('0')

    gamma, epsilon = 0, 0
    gamma_bits.reverse()
    for n, bit in enumerate(gamma_bits):
        if bit == '1':
            gamma += 2**n
        else:
            epsilon += 2**n
    
    return gamma * epsilon

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Solve day3 exercise')
    parser.add_argument('file', type=pathlib.Path, help='input file')

    args = parser.parse_args()

    inputs = read_report(args.file)
    print(solve(inputs))
