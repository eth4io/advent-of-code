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



# test
test_input_file = 'test_input.txt'
test_part_1_expected = 36
test_part_2_expected = 81

# real
input_file = 'input.txt'
part_1_expected = 794
part_1_expected_false = []

part_2_expected = 1706
part_2_expected_false = []

solve(day=Day, script_path=__file__,
      test_input_file=test_input_file, input_file=input_file,
      test_part_1_expected=test_part_1_expected, test_part_2_expected=test_part_2_expected,
      part_1_expected=part_1_expected, part_2_expected=part_2_expected,
      part_1_expected_false=part_1_expected_false, part_2_expected_false=part_2_expected_false,
      )
