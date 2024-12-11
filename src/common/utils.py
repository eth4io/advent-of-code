import collections
import os
import re
from enum import Enum
from collections import Counter, defaultdict, OrderedDict
from itertools import combinations
from sortedcontainers import SortedDict
from typing import Callable
from src.common.base_solution import Solution
from src.common.colour_utils import colourify, Colour
from src.common.grid import Grid, Direction, DIRECTIONS_4, DIRECTIONS_8
from src.common.graph import Graph
from src.common.base_solution import Result
from functools import cache


def _verify(title: str, result: Result,
           expected: int = None, expected_false: int or str or list[int] or list[str] = None) -> bool:
  display_time = f"time: {colourify(Colour.PINK, f'{result.total_time:.2f}')}s"
  if expected is None:
    is_expected_false = isinstance(expected_false, list) and result.result in expected_false \
                        or isinstance(expected_false, int or str) and result.result == expected_false
    if is_expected_false:
      display_result = f"{colourify(Colour.RED, '[fail]')} {colourify(Colour.RED, result.result)} <- expected false result"
    else:
      display_result = f"{colourify(Colour.ORANGE, '[submit]')} {colourify(Colour.ORANGE, result.result)}"

  else:
    if result.result == expected:
      display_result = f"{colourify(Colour.GREEN, '[pass]')} {colourify(Colour.GREEN, result.result)}"
    else:
      display_result = f"{colourify(Colour.RED, '[fail]')} {colourify(Colour.GREEN, result.result)} != expected {colourify(Colour.GREEN, expected)}"

  display = ' | '.join([title, display_result, display_time])
  print(display)

  return result.result == expected


def _solve(day: Solution.__class__, method: Callable, title: str,
          expected: int=None, expected_false: int or str or list[int] or list[str]=None):
  result = day.get_result(method)
  return result.result is not None and _verify(title, result, expected, expected_false)


def solve(day: Solution.__class__, script_path: str,
          test_input_file: str = 'test_input.txt', input_file: str = 'input.txt',
          test_part_1_expected: int or str=None, test_part_2_expected: int or str=None,
          part_1_expected: int or str=None, part_2_expected: int or str=None,
          part_1_expected_false: int or str or list[int] or list[str]=None,
          part_2_expected_false: int or str or list[int] or list[str]=None,
          ):
  test = day(script_path, test_input_file)
  real = day(script_path, input_file)

  print(colourify(Colour.LIGHT_BLUE, '------- part 1 -------'))
  if test.part_1 and _solve(day=test, title='test', method=test.part_1, expected=test_part_1_expected):
    _solve(day=real, title='real', method=real.part_1, expected=part_1_expected, expected_false=part_1_expected_false)

  print()
  print(colourify(Colour.LIGHT_BLUE, '------- part 2 -------'))
  if test.part_2 and _solve(day=test, title='test', method=test.part_2, expected=test_part_2_expected):
    _solve(day=real, title='real', method=real.part_2, expected=part_2_expected, expected_false=part_2_expected_false)

