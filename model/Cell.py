# author: Hendrik Werner
class Cell:
    def __init__(self, sudoku, row, column, block):
        self.value = 0
        self.sudoku = sudoku
        self.row = row
        self.column = column
        self.block = block

    def set_value(self, new_value):
        assert new_value in range(1, 10)
        self.value = new_value
        self.row.remove(self.value)
        self.column.remove(self.value)
        self.block.remove(self.value)

    def clear(self):
        if self.value:
            self.row.add(self.value)
            self.column.add(self.value)
            self.block.add(self.value)
            self.value = 0
