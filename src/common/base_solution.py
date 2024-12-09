from src.common.io_helper import read_input, input_lines
from src.common.colour_utils import colourify, Colour
from time import time
from typing import Callable
from dataclasses import dataclass

@dataclass
class Result:
  result: int or str
  setup_time: float
  run_time: float
  total_time: float


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


  def get_result(self, method: Callable) -> Result:
    t0 = time()
    self.setup()

    setup_time = time() - t0
    if setup_time >= 1:
      print(f'setup time: {setup_time:.2f}s')
      print(f"setup time: {colourify(Colour.PINK, f'{setup_time:.2f}')}s")

    result = method()

    total_time = time() - t0

    return Result(result=result, setup_time=setup_time, total_time=total_time, run_time=total_time-setup_time)
