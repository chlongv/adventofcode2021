import argparse
import pathlib
import tokenize
import typing

def read_commands(command_file: pathlib.Path) -> typing.List:
    with open(command_file) as f:
        commands = f.readlines()

    return [c.replace('\n','').split(' ') for c in commands]

def solve(commands) -> int:
    depth, horizontal = 0, 0
    for command in commands:
        c, step = command[0], int(command[1])
        if c == 'up':
            depth -= step
        elif c == 'down':
            depth += step
        elif c == 'forward':
            horizontal += step
        
    return horizontal * depth

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Solve day2 exercise')
    parser.add_argument('command_file', type=pathlib.Path, help='command input file')

    args = parser.parse_args()

    commands = read_commands(args.command_file)
    print(solve(commands))
