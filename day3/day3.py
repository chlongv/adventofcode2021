import argparse
import copy
import pathlib

def read_report(file: pathlib.Path):
    with open(file) as f:
        binaries = f.readlines()

    # get all chars
    lines = [[c for c in b.replace('\n', '')] for b in binaries]
    transpose = []
    for j, _ in enumerate(lines[0]):
        col = []
        for l in lines:
            col.append(l[j])
        transpose.append(col)
    return transpose, lines

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

def count_ones(lines, col):
    ones, zeros = 0, 0
    for l in lines:
        if l[col] == '1':
            ones += 1
        else:
            zeros += 1
    return ones, zeros

def prune_lines(c, col, lines):
    for j, l in reversed(list(enumerate(lines))):
        if l[col] is not c:
            lines.pop(j)

def compute_oxygen(lines):
    i = 0
    while len(lines) > 1:
        ones, zeros = count_ones(lines, i)
        keep_char = '1' if ones >= zeros else '0'
        prune_lines(keep_char, i, lines)
        i += 1

    bits = lines[0]
    bits.reverse()
    oxygen = 0
    for n, bit in enumerate(bits):
        if bit == '1':
            oxygen += 2**n
    return oxygen


def compute_co2(lines):
    i = 0
    while len(lines) > 1:
        ones, zeros = count_ones(lines, i)
        keep_char = '1' if ones < zeros else '0'
        prune_lines(keep_char, i, lines)
        i += 1

    bits = lines[0]
    bits.reverse()
    co2 = 0
    for n, bit in enumerate(bits):
        if bit == '1':
            co2 += 2**n
    return co2

def solve_support(lines):
    oxygen = compute_oxygen(copy.deepcopy(lines))
    co2 = compute_co2(copy.deepcopy(lines))
    return oxygen * co2

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Solve day3 exercise')
    parser.add_argument('file', type=pathlib.Path, help='input file')

    args = parser.parse_args()

    transpose, lines = read_report(args.file)
    print(solve(transpose))
    print(solve_support(lines))
