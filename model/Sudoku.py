# author: Hendrik Werner
from model.Cell import Cell


class Sudoku:
    def __init__(self):
        self.cells = []
        self.empty = []
        rows = []
        columns = []
        blocks = []
        for i in range(9):
            rows.append({*range(1, 10)})
            columns.append({*range(1, 10)})
        for x in range(3):
            blocks.append([])
            for y in range(3):
                blocks[x].append({*range(1, 10)})
        for x in range(9):
            for y in range(9):
                self.cells.append(Cell(
                    self,
                    rows[y],
                    columns[x],
                    blocks[x // 3][y // 3]
                ))

    def __str__(self):
        s = ""
        for i in range(81):
            s += str(self.cells[i])
            s += "\n" if (i + 1) % 9 == 0 else " "
        return s
