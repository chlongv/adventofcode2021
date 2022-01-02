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


def update_translator_first_pass(digit: str, trans: typing.Dict) -> None:
    if len(digit) == 2:
        trans['1'] = digit
    elif len(digit) == 3:
        trans['7'] = digit
    elif len(digit) == 4:
        trans['4'] = digit
    elif len(digit) == 7:
        trans['8'] = digit


def update_translator_second_pass(digit: str, trans: typing.Dict) -> None:
    if len(digit) == 6:
        # 0, 6, 9
        if set(trans['4']).issubset(set(digit)):
            trans['9'] = digit
        elif set(trans['1']).issubset(set(digit)):
            trans['0'] = digit
        else:
            # 6
            trans['6'] = digit


def update_translator_third_pass(digit: str, trans: typing.Dict) -> None:
    if len(digit) == 5:
        # 2, 3, 5
        if set(trans['1']).issubset(set(digit)):
            trans['3'] = digit
        elif set(digit).issubset(set(trans['9'])):
            trans['5'] = digit
        else:
            trans['2'] = digit


def decode(input: typing.List, trans: typing.Dict) -> int:
    dec = ''
    for d in input:
        for k,v in trans.items():
            if set(d) == set(v):
                dec += k
    return int(dec)

def decode_lines(signals: typing.List, outputs: typing.List, debug: bool) -> int:
    output_values = []
    for signal, output in zip(signals, outputs):
        line = signal + output
        translator = {}
        for digit in line:
            update_translator_first_pass(digit, translator)
        for digit in line:
            update_translator_second_pass(digit, translator)
        for digit in line:
            update_translator_third_pass(digit, translator)
        if debug:
            print(translator)
        output_values.append(decode(output, translator))
    return sum(output_values)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Solve day8 exercise')
    parser.add_argument('file', type=pathlib.Path, help='input file')
    parser.add_argument('-d', '--debug', action='store_true', help='debug')

    args = parser.parse_args()

    signals, outputs = read_input(args.file)
    print(find_unique_segments(outputs))
    print(decode_lines(signals, outputs, args.debug))