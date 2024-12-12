from src.common.utils import *

class Day(Solution):

  def setup(self):
    self.g = Grid(self.input_lines)


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



  def part_2(self):
    pass



# setup
test_input_file, input_file = 'test_input.txt', 'input.txt'
test, real = Day(__file__, test_input_file, '[test]'), Day(__file__, input_file, '[real]')

# part 1
print(colourify(Colour.LIGHT_BLUE, '------- part 1 -------'))
assert_equal(lambda: test.part_1(), 1930, title=test.title)
assert_equal(lambda: real.part_1(), 1483212, title=real.title)

# part 2
print(colourify(Colour.LIGHT_BLUE, '\n------- part 2 -------'))
assert_equal(lambda: real.part_2(), None, title=real.title)
assert_equal(lambda: real.part_2(), None, title=real.title)
