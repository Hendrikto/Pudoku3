# author: Hendrik Werner
class Cell:
    allowed = range(1, 10)

    def __init__(self, sudoku, row, column, block):
        self.value = 0
        self.sudoku = sudoku
        self.row = row
        self.column = column
        self.block = block
        sudoku.empty.append(self)

    def set_value(self, new_value):
        assert new_value in self.allowed
        self.clear()
        self.value = new_value
        self.row.remove(self.value)
        self.column.remove(self.value)
        self.block.remove(self.value)
        self.sudoku.empty.remove(self)

    def clear(self):
        if self.value:
            self.row.add(self.value)
            self.column.add(self.value)
            self.block.add(self.value)
            self.value = 0
            self.sudoku.empty.append(self)

    def get_candidates(self):
        return self.row & self.column & self.block

    def __str__(self):
        return str(self.value)
