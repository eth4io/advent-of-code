from src.common.utils import *

class Day(Solution):

  def setup(self):
    self.lines = self.input_lines
    self.stones = list(map(int, self.lines[0].split()))


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


  def part_1(self, blinks: int):
    return sum(self.split(stone, blinks) for stone in self.stones)


  def part_2(self, blinks: int):
    return sum(self.split(stone, blinks) for stone in self.stones)



# setup
test_input_file, input_file = 'test_input.txt', 'input.txt'
test, real = Day(__file__, test_input_file, '[test]'), Day(__file__, input_file, '[real]')

# part 1
print(colourify(Colour.LIGHT_BLUE, '------- part 1 -------'))
assert_equal(lambda: test.part_1(6), 22, test.title)
assert_equal(lambda: test.part_1(25), 55312, test.title)
assert_equal(lambda: real.part_1(25), 184927, real.title)

# part 2
print(colourify(Colour.LIGHT_BLUE, '\n------- part 2 -------'))
assert_equal(lambda: real.part_2(75), 220357186726677, real.title)
assert_equal(lambda: real.part_2(75), title=real.title)
