from argparse import ArgumentParser
from pudoku import *

import sys


def parse_args():
    parser = ArgumentParser()
    parser.add_argument(
        "seed",
        type=str,
        help="Sudoku seed like \"123...456\""
    )
    parser.add_argument(
        "-p", "--pretty",
        action="store_true",
        help="print Sudokus in a human readable grid",
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    stringifier = PrettyStringifier() if args.pretty else SimpleStringifier()
    sudoku = Sudoku(seed=args.seed, stringifier=stringifier)
    solver = SudokuSolver(sudoku).solve()
    print(sudoku)
