
from src.common.utils import *

class Day(Solution):

  def setup(self):
    self.lines = self.input_lines
    self.stones = [int(stone) for stone in self.lines[0].split(' ')]


  @cache
  def split(self, num: int, n: int) -> int:
    if n == 0:
      return 1
    if num == 0:
      return self.split(1, n-1)
    size = len(str(num))
    if size % 2 == 0 and size >= 2:
      mid = size // 2
      left = int(str(num)[:mid])
      right = int(str(num)[mid:])
      return self.split(left, n-1) + self.split(right, n-1)
    return self.split(num* 2024, n-1)


  def part_1(self):
    ret = 0
    for stone in self.stones:
      ret += self.split(stone, 25)

    return ret


  def part_2(self):
    ret = 0
    for stone in self.stones:
      ret += self.split(stone, 75)
    return ret



test_input_file = 'test_input.txt'
input_file = 'input.txt'

# part 1
test_part_1_expected = 55312
part_1_expected = 184927
part_1_expected_false = []

# part 2
test_part_2_expected = 65601038650482
part_2_expected = 220357186726677
part_2_expected_false = []

solve(day=Day, script_path=__file__,
      test_input_file=test_input_file, input_file=input_file,
      test_part_1_expected=test_part_1_expected, test_part_2_expected=test_part_2_expected,
      part_1_expected=part_1_expected, part_2_expected=part_2_expected,
      part_1_expected_false=part_1_expected_false, part_2_expected_false=part_2_expected_false,
      )
