# author: Hendrik Werner
class Area(set):
    """
    A set of integers that is initialized to contain all legal values for a
    Sudoku (1..9).
    """

    def __init__(self):
        super().__init__()
        self.update(range(1, 10))
