# author: Hendrik Werner
class Area(set):
    def __init__(self):
        super().__init__()
        self.update(range(1, 10))
