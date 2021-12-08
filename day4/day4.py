import argparse
import copy
import numpy as np
import pathlib

class Bingo:
    GRID_SIZE = 5

    def __init__(self, grid: np.ndarray):
        self.grid = grid
        self.result = np.zeros((Bingo.GRID_SIZE, Bingo.GRID_SIZE), dtype=bool)
    
    def __str__(self):
        return str(self.result) + '\n' + str(self.grid)
    
    def play_number(self, n: int) -> bool:
        mask = np.isin(self.grid, n)
        self.result = np.logical_or(self.result, mask)
        return self.check_bingo()

    def check_bingo(self) -> bool:
        lines = np.all(self.result, axis=0)
        cols = np.all(self.result, axis=1)
        # diag1 = np.diagonal(self.result)
        # diag2 = np.fliplr(self.result).diagonal()
        # diag = np.logical_or(np.all(diag1), np.all(diag2))
        return np.any(lines) or np.any(cols) # or diag.any()
    
    def score(self, n: int) -> int:
        internal_score = 0
        for r, s in np.nditer([self.result, self.grid]):
            if not r:
                internal_score += s
        return internal_score * n


    @staticmethod
    def read_bingo(file: pathlib.Path):
        grids = []
        with open(file) as f:
            lines = f.readlines()
            numbers = [int(n) for n in lines[0].split(',')]

        nb_lines = len(lines)
        for i in range(2, nb_lines, 6):
            array = np.zeros((Bingo.GRID_SIZE,Bingo.GRID_SIZE), dtype=int)
            grid = lines[i:i+5]
            for i, l in enumerate(grid):
                array[i] = [int(n) for n in l.split()]
            grids.append(Bingo(array))
            
        return numbers, grids

    @staticmethod
    def play(numbers, grids) -> int:
        for n in numbers:
            for g in grids:
                if g.play_number(n):
                    print('!!! FIRST BINGO !!!')
                    print(n)
                    print(g)
                    return g.score(n)

    @staticmethod
    def play_until_last(numbers, grids) -> int:
        for n in numbers:
            remove = []
            for g in grids:
                if g.play_number(n):
                    print('!! BINGO !!')
                    if len(grids) > 1:
                        print(f'Removing grid, {len(grids)-1} remaining')
                        print(n)
                        remove.append(g) # don't remove it directly here, messes the for loop
                    else:
                        print('!!! LAST GRID BINGO !!!')
                        print(n)
                        print(g)
                        return g.score(n)
            for r in remove:
                grids.remove(r)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Solve day4 exercise')
    parser.add_argument('file', type=pathlib.Path, help='input file')

    args = parser.parse_args()

    numbers, grids = Bingo.read_bingo(args.file)
    print(Bingo.play(copy.deepcopy(numbers),copy.deepcopy(grids)))
    print(Bingo.play_until_last(numbers, grids))
