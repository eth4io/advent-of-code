from src.common.io_helper import read_input, input_lines
from src.common.colour_utils import colourify, Colour
from time import time
from typing import Callable

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


  def solve(self, title: str, method: Callable, expected: int=None) -> bool:
    t0 = time()
    self.setup()

    setup_time = time() - t0
    if setup_time >= 1:
      print(f'setup time: {setup_time:.2f}s')
      print(f"setup time: {colourify(Colour.PINK, f'{setup_time:.2f}')}s")

    result = method()

    total_time = time() - t0
    display_time = f"time: {colourify(Colour.PINK, f'{total_time:.2f}')}s"
    if expected is None:
      display_result = f"result: {colourify(Colour.ORANGE, result)}"
    else:
      if result == expected:
        display_result = f"{colourify(Colour.GREEN, '[pass]')} result: {colourify(Colour.GREEN, result)} == expected {colourify(Colour.GREEN, expected)}"
      else:
        display_result = f"{colourify(Colour.RED, '[fail]')} result: {colourify(Colour.GREEN, result)} != expected {colourify(Colour.GREEN, expected)}"

    display = ' | '.join([title, display_result, display_time])
    print(display)
    return result == expected
