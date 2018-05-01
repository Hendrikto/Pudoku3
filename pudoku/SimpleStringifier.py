# author: Hendrik Werner
from .SudokuStringifier import SudokuStringifier


class SimpleStringifier(SudokuStringifier):
    def stringify(self, sudoku):
        return "".join(map(str, sudoku.cells))
