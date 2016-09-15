# author: Hendrik Werner
from model import Area
from model import SimpleStringifier
from model.Cell import Cell


class Sudoku:
    def __init__(self, seed="", stringifier=None):
        self.cells = []
        self.empty = []
        self.stringifier = stringifier or SimpleStringifier()
        rows = [Area() for _ in range(9)]
        columns = [Area() for _ in range(9)]
        blocks = [[Area() for _ in range(3)] for _ in range(3)]
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
