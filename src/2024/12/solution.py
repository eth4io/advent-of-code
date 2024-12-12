from src.common.utils import *

class Day(Solution):

  def setup(self):
    self.g = Grid(self.input_lines)


  def calc(self, plots: set[tuple[int, int]]):
    peri = 0
    for plot in plots:
      for next in self.g.get_all_moved(DIRECTIONS_4, plot):
        if not self.g.is_in_range(next) or next not in plots:
          peri += 1

    return peri * len(plots)


  def part_1(self):
    all_visited = set()
    costs = []
    for r, row in enumerate(self.g.grid):
      for c, value in enumerate(row):
        cell = (r, c)
        if cell not in all_visited:
          visited = set()
          dfs = [cell]
          for cur in dfs:
            visited.add(cur)
            for next in self.g.get_all_in_range_moved(DIRECTIONS_4, cur):
              if next not in visited and next not in all_visited and self.g.get(next) == value:
                dfs.append(next)

          costs.append(self.calc(visited))
          all_visited = all_visited.union(visited)

    return sum(costs)



  def part_2(self):
    pass



# setup
test_input_file, input_file = 'test_input.txt', 'input.txt'
test, real = Day(__file__, test_input_file, '[test]'), Day(__file__, input_file, '[real]')

# part 1
print(colourify(Colour.LIGHT_BLUE, '------- part 1 -------'))
assert_equal(lambda: test.part_1(), 1930, title=test.title)
assert_equal(lambda: real.part_1(), None, title=real.title)

# part 2
print(colourify(Colour.LIGHT_BLUE, '\n------- part 2 -------'))
assert_equal(lambda: real.part_2(), None, title=real.title)
assert_equal(lambda: real.part_2(), None, title=real.title)
