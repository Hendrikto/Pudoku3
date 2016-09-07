# author: Hendrik Werner
from model import Area
from model import PrettyStringifier
from model.Cell import Cell


class Sudoku:
    def __init__(self, seed="", stringifier=None):
        self.cells = []
        self.empty = []
        self.stringifier = stringifier or PrettyStringifier()
        rows = []
        columns = []
        blocks = []
        for i in range(9):
            rows.append(Area())
            columns.append(Area())
        for x in range(3):
            blocks.append([])
            for y in range(3):
                blocks[x].append(Area())
        for x in range(9):
            for y in range(9):
                self.cells.append(Cell(
                    self,
                    rows[y],
                    columns[x],
                    blocks[x // 3][y // 3]
                ))
        self._parse(seed)

    def _parse(self, seed):
        for i in range(min(len(seed), 81)):
            try:
                self.cells[i].set_value(int(seed[i]))
            except ValueError:
                pass

    def __str__(self):
        return self.stringifier.stringify(self)
