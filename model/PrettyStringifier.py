# author: Hendrik Werner
from model.SudokuStringifier import SudokuStringifier


class PrettyStringifier(SudokuStringifier):
    def stringify(self, sudoku):
        s = ""
        for i in range(81):
            s += str(sudoku.cells[i])
            s += "\n" if (i + 1) % 9 == 0 else " "
        return s
