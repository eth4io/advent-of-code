from collections import defaultdict
from enum import Enum

class Direction(Enum):
  # [dy, dx]
  UP = [-1, 0]
  RIGHT = [0, 1]
  DOWN = [1, 0]
  LEFT = [0, -1]
  UP_RIGHT = [-1, 1]
  DOWN_RIGHT = [1, 1]
  DOWN_LEFT = [1, -1]
  UP_LEFT = [-1, -1]
  


DIRECTIONS_4 = [Direction.UP, Direction.RIGHT, Direction.DOWN, Direction.LEFT]
DIRECTIONS_8 = [Direction.UP, Direction.UP_RIGHT, Direction.RIGHT, Direction.DOWN_RIGHT, Direction.DOWN, Direction.DOWN_LEFT, Direction.LEFT, Direction.UP_LEFT]
DIRECTIONS_DIAGONAL = [Direction.UP_RIGHT, Direction.DOWN_RIGHT, Direction.DOWN_LEFT, Direction.UP_LEFT]


class Grid:
  grid: list[list[str or int]]
  y_n: int
  x_n: int
  cell_map: defaultdict


  def __init__(self, lines: list[str]):
    self.grid = [[c for c in line] for line in lines]
    self.y_n = len(self.grid)
    self.x_n = len(self.grid[0])
    self.cell_map = defaultdict(list)


  def __str__(self):
    lines = ''
    for row_index, row in enumerate(self.grid):
      line = [f'{cell}' for cell in row]
      lines += (' '.join(line)) + '\n'
    return lines


  def to_int(self):
    self.grid = [[int(cell) for cell in row] for row in self.grid]
    return self


  def get(self, coordinates: [tuple[int, int] or list[int, int] or int], x: int = None):
    if isinstance(coordinates, tuple) or isinstance(coordinates, list):
      y, x = coordinates
    else:
      y = coordinates
    return self.grid[y][x]


  def get_all_moved(self, directions: list[Direction], coordinates: [tuple[int, int] or list[int, int] or int], x: int = None) -> list[tuple[int, int]]:
    if isinstance(coordinates, tuple) or isinstance(coordinates, list):
      y, x = coordinates
    else:
      y = coordinates
    cell = (y, x)
    all_moved = list(map(lambda direction: self.get_moved(direction, cell), directions))
    return all_moved


  def get_all_in_range_moved(self, directions: list[Direction], coordinates: [tuple[int, int] or list[int, int] or int], x: int = None) -> list[tuple[int, int]]:
    if isinstance(coordinates, tuple) or isinstance(coordinates, list):
      y, x = coordinates
    else:
      y = coordinates
    cell = (y, x)
    all_moved = list(map(lambda direction: self.get_moved(direction, cell), directions))
    all_in_range_moved = list(filter(lambda cell: self.is_in_range(cell), all_moved))
    return all_in_range_moved


  def is_in_range(self, coordinates: [tuple[int, int] or list[int, int] or int], x: int = None) -> bool:
    if isinstance(coordinates, tuple) or isinstance(coordinates, list):
      y, x = coordinates
    else:
      y = coordinates
    return 0 <= y < self.y_n and 0 <= x < self.x_n


  def build_cell_map(self):
    for row_index, row in enumerate(self.grid):
      for col_index, cell in enumerate(row):
        self.cell_map[cell].append((row_index, col_index))


  @staticmethod
  def get_moved(direction: Direction, coordinates: [tuple[int, int] or list[int, int] or int], x: int = None) -> tuple[int, int]:
    dy, dx = direction.value
    if isinstance(coordinates, tuple) or isinstance(coordinates, list):
      y, x = coordinates
    else:
      y = coordinates
    return y + dy, x + dx
