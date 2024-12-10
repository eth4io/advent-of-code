from src.common.utils import *

class Day(Solution):

  def setup(self):
    self.g = Grid(self.input_lines, True)
    self.score = [[0] * self.g.x_n for _ in range(self.g.y_n)]


  def part_1(self):

    ret = 0
    for y in range(self.g.y_n):
      for x in range(self.g.x_n):
        visited = set()
        if self.g.get(y, x) != 0:
          continue

        dfs = [(y, x)]

        for cur_y, cur_x in dfs:
          if self.g.get(cur_y, cur_x) == 9 and (cur_y, cur_x) not in visited:
            ret += 1
            visited.add((cur_y, cur_x))
          for dir in DIRECTIONS_4:
            new_y, new_x = self.g.get_moved(dir, cur_y, cur_x)
            if self.g.is_in_range(new_y, new_x) and self.g.get(new_y, new_x) == self.g.get(cur_y, cur_x)+1:
              dfs.append((new_y, new_x))

    return ret


  def part_2(self):
    ret = 0
    for i in range(9, -1, -1):
      for y in range(self.g.y_n):
        for x in range(self.g.x_n):
          if self.g.get(y, x) != i:
            continue
          if i == 9:
            self.score[y][x] = 1
            continue

          for dir in DIRECTIONS_4:
            new_y, new_x = self.g.get_moved(dir, y, x)
            if self.g.is_in_range(new_y, new_x) and self.g.get(new_y, new_x) == i+1:
              self.score[y][x] += self.score[new_y][new_x]

          if i == 0:
            ret += self.score[y][x]


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
