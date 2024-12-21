import collections
import sys
import os
import threading
import re
from enum import Enum
from collections import Counter, defaultdict, OrderedDict, deque
from itertools import combinations
from sortedcontainers import SortedDict
from typing import Callable
from src.common.base_solution import Solution
from src.common.colour_utils import colourify, Colour
from src.common.grid import Grid, Direction, DIRECTIONS_4, DIRECTIONS_8, DIRECTIONS_VERTICAL, DIRECTIONS_HORIZONTAL, DIRECTIONS_DIAGONAL
from src.common.graph import Graph
from functools import cache
from time import time
from dataclasses import dataclass
import inspect

# sys.setrecursionlimit(10**9)

@dataclass
class Result:
  result: int or str
  duration: float


def get_result(method: Callable[..., any]) -> Result:
  t0 = time()
  result = method()

  return Result(result=result, duration=time()-t0)


def assert_equal(func: Callable[..., any], expected: any=None, title: str=None, description: str=None) -> bool:
  result = get_result(lambda: func())

  display_time = f"time: {colourify(Colour.PINK, f'{result.duration:.2f}')}s"

  if expected is None:
    display_result = f"{colourify(Colour.ORANGE, '[submit]')} {colourify(Colour.ORANGE, result.result)}"
    printx([title, display_result, display_time, description])
    return False
  is_expected = result.result == expected
  if is_expected:
    display_result = f"{colourify(Colour.GREEN, '[pass]')} {colourify(Colour.GREEN, result.result)}"
  else:
    display_result = f"{colourify(Colour.RED, '[fail]')} {colourify(Colour.RED, result.result)} != expected {colourify(Colour.GREEN, expected)}"

  printx([title, display_result, display_time, description])
  return is_expected


def assert_not_equal(func: Callable[..., any], expected: any=None, title: str=None, description: str=None) -> bool:
  result = get_result(lambda: func())

  display_time = f"time: {colourify(Colour.PINK, f'{result.duration:.2f}')}s"

  if expected is None:
    display_result = f"{colourify(Colour.ORANGE, '[submit]')} {colourify(Colour.ORANGE, result.result)}"
    printx([title, display_result, display_time, description])
    return False
  is_expected = result.result == expected
  if not is_expected:
    display_result = f"{colourify(Colour.GREEN, '[pass]')} {colourify(Colour.GREEN, result.result)} != expected false {colourify(Colour.RED, expected)}"
  else:
    display_result = f"{colourify(Colour.RED, '[fail]')} {colourify(Colour.RED, result.result)} == expected false {colourify(Colour.GREEN, expected)}"

  printx([title, display_result, display_time, description])
  return is_expected


def printx(items: list[str]):
  display = ' | '.join(filter(lambda x: x is not None, items))
  print(display)
