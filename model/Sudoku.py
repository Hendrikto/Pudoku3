# author: Hendrik Werner
from model.Cell import Cell


class Sudoku:
    cells = []
    empty = []

    def __init__(self):
        rows = []
        columns = []
        blocks = []
        for i in range(9):
            rows.append([*range(1, 10)])
            columns.append([*range(1, 10)])
        for x in range(3):
            blocks.append([])
            for y in range(3):
                blocks[x].append([*range(1, 10)])
        for x in range(9):
            for y in range(9):
                self.cells.append(Cell(
                    self,
                    rows[y],
                    columns[x],
                    blocks[x // 3][y // 3]
                ))
