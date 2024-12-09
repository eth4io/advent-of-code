import collections
import os
import re
from enum import Enum
from collections import Counter, defaultdict, OrderedDict
from sortedcontainers import SortedDict
from itertools import combinations
from src.common.base_solution import Solution
from src.common.colour_utils import colourify, Colour
from src.common.grid import Grid, Direction, DIRECTIONS_4, DIRECTIONS_8
from src.common.graph import Graph

def solve(day: Solution.__class__, script_path: str,
          test_input_file: str = 'test_input.txt', input_file: str = 'input.txt',
          test_part_1_expected: int or str=None, test_part_2_expected: int or str=None,
          part_1_expected: int or str=None, part_2_expected: int or str=None,
          ):
  test = day(script_path, test_input_file)
  real = day(script_path, input_file)

  print(colourify(Colour.LIGHT_BLUE, '------- part 1 -------'))
  if test.part_1 and test.solve(title='test', method=test.part_1, expected=test_part_1_expected):
    real.solve(title='real', method=real.part_1, expected=part_1_expected)

  print()
  print(colourify(Colour.LIGHT_BLUE, '------- part 2 -------'))
  if test.part_2 and test.solve(title='test', method=test.part_2, expected=test_part_2_expected):
    real.solve(title='real', method=real.part_2, expected=part_2_expected)

