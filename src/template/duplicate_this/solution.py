from src.common.utils import *

class Day(Solution):

  def setup(self):
    self.lines = self.input_lines


  def part_1(self):
    pass


  def part_2(self):
    pass



# setup
test_input_file, input_file = 'test_input.txt', 'input.txt'
test, real = Day(__file__, test_input_file, '[test]'), Day(__file__, input_file, '[real]')

# part 1
print(colourify(Colour.LIGHT_BLUE, '------- part 1 -------'))
assert_equal(lambda: test.part_1(), None, title=test.title)
assert_equal(lambda: real.part_1(), None, title=real.title)

# part 2
print(colourify(Colour.LIGHT_BLUE, '\n------- part 2 -------'))
assert_equal(lambda: real.part_2(), None, title=real.title)
assert_equal(lambda: real.part_2(), None, title=real.title)
