from src.common.io_helper import read_input, input_lines
from src.common.colour_utils import colourify, Colour
from time import time
from typing import Callable


class Solution:
  input: str
  input_lines: list[str]
  title: str

  def __init__(self, script_file=__file__, input_filename='input.txt', title: str=None):
    self.input = read_input(script_file, input_filename)
    self.input_lines = input_lines(self.input)
    self.title = title

    self.setup_with_profiling()


  def setup(self):
    pass


  def setup_with_profiling(self):
    t0 = time()
    self.setup()

    setup_time = time() - t0
    if setup_time >= 1:
      print(f"setup {self.title} took: {colourify(Colour.PINK, f'{setup_time:.2f}')}s")


  def part_1(self, *args, **kwargs):
    print('no part 1')


  def part_2(self, *args, **kwargs):
    print('no part 2')


