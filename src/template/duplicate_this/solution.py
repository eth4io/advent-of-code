from src.common.utils import *


class Day(Solution):

  def setup(self):
    pass


  def part_1(self):
    pass


  def part_2(self):
    pass



# test
test_input_file = 'test_input.txt'
test_part_1_expected = None
test_part_2_expected = None

# real
input_file = 'input.txt'
part_1_expected = None
part_1_expected_false = [None]

part_2_expected = None
part_2_expected_false = [None]

solve(day=Day, script_path=__file__,
      test_input_file=test_input_file, input_file=input_file,
      test_part_1_expected=test_part_1_expected, test_part_2_expected=test_part_2_expected,
      part_1_expected=part_1_expected, part_2_expected=part_2_expected,
      part_1_expected_false=part_1_expected_false, part_2_expected_false=part_2_expected_false,
      )
