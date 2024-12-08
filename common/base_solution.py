from common.io_helper import read_input, input_lines
from time import time

class Solution:
  input: str
  input_lines: list[str]

  def __init__(self, script_file=__file__, input_filename='input.txt'):
    self.input = read_input(script_file, input_filename)
    self.input_lines = input_lines(self.input)
    self._counted_results = None


  def setup(self):
    pass


  def part_1(self):
    print('no part 1')


  def part_2(self):
    print('no part 2')


  def solve(self):
    self.solve_part_1()
    self.solve_part_2()


  def solve_part_1(self):
    t0 = time()
    self.setup()

    setup_time = time() - t0
    if setup_time >= 1:
      print(f'setup time: {setup_time:.2f}s')

    result = self.part_1()

    total_time = time() - t0
    print("------------")
    print(f"part 1 result: {result}")
    print(f"part 1 time: {total_time:.2f}s")
    print("------------")


  def solve_part_2(self):
    t0 = time()
    self.setup()

    setup_time = time() - t0
    if setup_time >= 1:
      print(f'setup time: {setup_time:.2f}s')

    result = self.part_2()

    total_time = time() - t0
    print("------------")
    print(f"part 2 result: {result}")
    print(f"part 2 time: {total_time:.2f}s")
    print("------------")
