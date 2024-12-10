from enum import Enum

class Direction(Enum):
    # [dy, dx]
    UP = [-1, 0]
    DOWN = [1, 0]
    LEFT = [0, -1]
    RIGHT = [0, 1]
    UP_LEFT = [-1, -1]
    UP_RIGHT = [-1, 1]
    DOWN_LEFT = [1, -1]
    DOWN_RIGHT = [1, 1]


DIRECTIONS_4 = [Direction.UP, Direction.RIGHT, Direction.DOWN, Direction.LEFT]
DIRECTIONS_8 = [Direction.UP, Direction.UP_RIGHT, Direction.RIGHT, Direction.DOWN_RIGHT, Direction.DOWN, Direction.DOWN_LEFT, Direction.LEFT, Direction.UP_LEFT]


class Grid:
    grid: list[list[str or int]]
    y_n: int
    x_n: int


    def __init__(self, lines: list[str]):
        self.grid = [[int(c) for c in line] for line in lines]
        self.y_n = len(self.grid)
        self.x_n = len(self.grid[0])


    def get(self, r, c):
        return self.grid[r][c]


    def get_moved(self, direction: Direction, coordinates: [tuple[int, int] or list[int, int] or int], x: int = None) -> tuple[int, int]:
        dy, dx = direction.value
        if isinstance(coordinates, tuple) or isinstance(coordinates, list):
            y, x = coordinates
        else:
            y = coordinates
        return y + dy, x + dx


    def is_in_range(self, coordinates: [tuple[int, int] or list[int, int] or int], x: int = None) -> bool:
        if isinstance(coordinates, tuple) or isinstance(coordinates, list):
            y, x = coordinates
        else:
            y = coordinates
        return 0 <= y < self.y_n and 0 <= x < self.x_n



lines =["aaaa", "bbbb", "cccc"]



