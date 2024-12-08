import collections
import os
import re
from enum import Enum
from collections import Counter
from collections import defaultdict

dir = '2024/07'

input_file = 'input.txt'
# input_file = 'test_input.txt'

file_path = os.path.join(dir, input_file)

edges = []

with open(os.path.join(dir, input_file), 'r') as file:
    lines = [line.strip() for line in file]


def get_case(line: str):
    items = line.strip().split(':')
    ans = int(items[0])
    elements = [int(item) for item in items[1][1:].split(' ')]
    return elements, ans

cases = [get_case(line) for line in lines]

def is_valid(elements, ans) -> bool:
    dfs = [(elements[0], elements[1:])]

    while dfs:
        cur, remaining = dfs.pop()
        print(cur, remaining, dfs)
        if len(remaining) == 0:
            if cur == ans:
                return True
            else:
                continue
        next = remaining[0]
        if cur + next <= ans:
            dfs.append((cur + next, remaining[1:]))
        if cur * next <= ans:
            dfs.append((cur * next, remaining[1:]))

    return False


ret = 0
for elements, ans in cases:
    if is_valid(elements, ans):
        ret += ans




# part 2

def is_valid_2(elements, ans) -> bool:
    dfs = [(elements[0], elements[1:])]

    while dfs:
        cur, remaining = dfs.pop()
        print(cur, remaining, dfs)
        if len(remaining) == 0:
            if cur == ans:
                return True
            else:
                continue
        next = remaining[0]
        if cur + next <= ans:
            dfs.append((cur + next, remaining[1:]))
        if cur * next <= ans:
            dfs.append((cur * next, remaining[1:]))
        concat = int(str(cur) + str(next))
        if concat <= ans:
            dfs.append((concat, remaining[1:]))

    return False

ret_2 = 0
for elements, ans in cases:
    if is_valid_2(elements, ans):
        ret_2 += ans

