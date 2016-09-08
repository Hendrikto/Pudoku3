# author: Hendrik Werner
from model.SudokuStringifier import SudokuStringifier


class PrettyStringifier(SudokuStringifier):
    def stringify(self, sudoku):
        s = ""
        for i in range(81):
            cellID = i + 1
            if cellID != 1 and cellID % 27 == 1:
                s += "------+-------+------\n"
            s += str(sudoku.cells[i])
            if cellID % 9 == 0:
                s += "\n"
            elif cellID % 3 == 0:
                s += " | "
            else:
                s += " "
        return s
