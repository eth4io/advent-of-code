from src.common.utils import *

class Day(Solution):

  def setup(self):
    self.g = Grid(self.input_lines)
    self.lookup = {
      Direction.UP: [Direction.LEFT, Direction.RIGHT],
      Direction.DOWN: [Direction.LEFT, Direction.RIGHT],
      Direction.LEFT: [Direction.UP, Direction.DOWN],
      Direction.RIGHT: [Direction.UP, Direction.DOWN],
    }


  def part_1(self):
    all_visited = set()
    costs = 0
    for r, row in enumerate(self.g.grid):
      for c, value in enumerate(row):
        cell = (r, c)
        if cell not in all_visited:
          visited = set()
          dfs = [cell]
          visited.add(cell)
          peri = 0
          for cur in dfs:
            for next in self.g.get_all_moved(DIRECTIONS_4, cur):
              if not self.g.is_in_range(next) or self.g.get(next) != value:
                peri += 1
              elif self.g.is_in_range(next) and next not in visited and self.g.get(next) == value:
                visited.add(next)
                dfs.append(next)

          costs += peri * len(visited)
          all_visited = all_visited.union(visited)

    return costs


  def calc_line_cost(self, line: list[int]):
    if len(line) == 1:
      return 1

    line.sort()
    sides = 1
    for i in range(1, len(line)):
      if abs(line[i] - line[i-1]) != 1:
        sides += 1

    return sides


  def calc_edge_count(self, fences: set[tuple[int, int, dir]]):
    dict = defaultdict(list)
    for y, x, dir in fences:
      if dir in DIRECTIONS_HORIZONTAL: # fence would be vertical
        dict[(x, dir)].append(y)
      else: # fence would be horizontal
        dict[(y, dir)].append(x)

    total = 0
    for line in dict.values():
      total += self.calc_line_cost(line)

    return total


  def part_2(self):
    all_visited = set()
    costs = 0
    for r, row in enumerate(self.g.grid):
      for c, value in enumerate(row):
        cell = (r, c)
        if cell not in all_visited:
          visited = set()
          deq = deque([cell])
          visited.add(cell)
          fences = set()
          while deq:
            cur = deq.popleft()
            for dir in DIRECTIONS_4:
              next = self.g.get_moved(dir, cur)
              should_fence = not self.g.is_in_range(next) or self.g.get(next) != value
              if should_fence:
                fences.add((cur[0], cur[1], dir))
              elif self.g.is_in_range(next) and next not in visited and self.g.get(next) == value:
                visited.add(next)
                deq.append(next)
          costs += self.calc_edge_count(fences) * len(visited)
          all_visited = all_visited.union(visited)

    return costs


# setup
test_input_file, test_input_file_2, input_file = 'test_input.txt', 'test_input_2.txt', 'input.txt'
test, real = Day(__file__, test_input_file, '[test]'), Day(__file__, input_file, '[real]')
test2 = Day(__file__, test_input_file_2, '[test2]')
test3 = Day(__file__, 'test_input_3.txt', '[test3]')

# part 1
print(colourify(Colour.LIGHT_BLUE, '------- part 1 -------'))
assert_equal(lambda: test.part_1(), 1930, title=test.title)
assert_equal(lambda: real.part_1(), 1483212, title=real.title)

# part 2
print(colourify(Colour.LIGHT_BLUE, '\n------- part 2 -------'))
assert_equal(lambda: test.part_2(), 1206, title=test.title)
assert_equal(lambda: test2.part_2(), 236, title=test.title)
assert_equal(lambda: test3.part_2(), 368, title=test.title)
assert_not_equal(lambda: real.part_2(), 897298, title=real.title)
assert_equal(lambda: real.part_2(), None, title=real.title)
