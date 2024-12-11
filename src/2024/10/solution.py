from src.common.utils import *

class Day(Solution):

  def setup(self):
    self.g = Grid(self.input_lines).to_int()


  def part_1(self):

    ret = 0
    for y in range(self.g.y_n):
      for x in range(self.g.x_n):
        visited = set()
        if self.g.get(y, x) != 0:
          continue

        dfs = [(y, x)]

        for cur in dfs:
          if self.g.get(cur) == 9 and cur not in visited:
            ret += 1
            visited.add(cur)
          for new_cell in self.g.get_all_in_range_moved(DIRECTIONS_4, cur):
            if self.g.get(new_cell) == self.g.get(cur) + 1:
              dfs.append(new_cell)

    return ret


  def part_2(self):
    self.g.build_cell_map()
    score = [[0] * self.g.x_n for _ in range(self.g.y_n)]

    # 9
    for y, x in self.g.cell_map[9]:
      score[y][x] = 1

    # 8 - 0
    for i in range(8, -1, -1):
      for cur in self.g.cell_map[i]:
        y, x = cur
        for new_cell in self.g.get_all_in_range_moved(DIRECTIONS_4, cur):
          new_y, new_x = new_cell
          if self.g.get(new_cell) == self.g.get(cur) + 1:
            score[y][x] += score[new_y][new_x]

    ret = 0
    for y, x in self.g.cell_map[0]:
      ret += score[y][x]

    return ret



# setup
test_input_file, input_file = 'test_input.txt', 'input.txt'
test, real = Day(__file__, test_input_file), Day(__file__, input_file)

# part 1
print(colourify(Colour.LIGHT_BLUE, '------- part 1 -------'))
assert_equal(lambda: test.part_1(), 36, 'test')
assert_equal(lambda: real.part_1(), 794, 'real')

print()
# part 2
print(colourify(Colour.LIGHT_BLUE, '------- part 2 -------'))
assert_equal(lambda: test.part_2(), 81, 'test')
assert_equal(lambda: real.part_2(), 1706, 'real')
