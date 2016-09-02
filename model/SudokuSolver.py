# author: Hendrik Werner
class SudokuSolver:
    def __init__(self, sudoku):
        self.sudoku = sudoku

    def solve(self):
        if len(self.sudoku.empty) == 0:
            return True
        cell = self.sudoku.empty[0]
        for candidate in cell.get_candidates():
            cell.set_value(candidate)
            if self.solve():
                return True
        cell.clear()
        return False
