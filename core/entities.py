import core.input_constants
from screen import utils

_directions = {core.input_constants.UP: (0, -1), core.input_constants.DOWN: (0, 1),
               core.input_constants.LEFT: (-1, 0), core.input_constants.RIGHT: (1, 0)}

class Snake:
    nodes = []
    _direction = (0, 1)

    def __init__(self):
        self.nodes.append([3, 5])
        self.nodes.append([4, 5])
        self.nodes.append([5, 5])

    def on_input(self, key):
        if key in _directions.keys():
            self._direction = _directions[key]

    def update(self):
        self.nodes.append([sum(pair) for pair in zip(self.nodes[-1], self._direction)])
        self.nodes.pop(0)

    def render(self):
        for node in self.nodes:
            print(utils.pos('*', *node))
