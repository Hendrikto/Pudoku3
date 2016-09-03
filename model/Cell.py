# author: Hendrik Werner
class Cell:
    allowed = range(1, 10)

    def __init__(self, sudoku, row, column, block):
        self.__value = 0
        self.__sudoku = sudoku
        self.__row = row
        self.__column = column
        self.__block = block
        sudoku.empty.append(self)

    def set_value(self, new_value):
        assert new_value in self.allowed
        self.clear()
        self.__value = new_value
        self.__row.remove(self.__value)
        self.__column.remove(self.__value)
        self.__block.remove(self.__value)
        self.__sudoku.empty.remove(self)

    def clear(self):
        if self.__value:
            self.__row.add(self.__value)
            self.__column.add(self.__value)
            self.__block.add(self.__value)
            self.__value = 0
            self.__sudoku.empty.append(self)

    def get_candidates(self):
        return self.__row & self.__column & self.__block

    def __str__(self):
        return str(self.__value) if self.__value else "."
