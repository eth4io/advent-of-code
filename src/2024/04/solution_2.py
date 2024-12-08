import collections
import os
import re
from enum import Enum

input_file = 'input.txt'
# input_file = 'test_input2.txt'
dir = '2024/04'

file_path = os.path.join(dir, input_file)


with open(file_path, 'r') as file:
    # Read and process each line, stripping whitespace
    g = [line.strip() for line in file]


# part 1
r_size = len(g)
c_size = len(g[0])

patterns = [
    ['M', 'M',
     'S', 'S'],
    ['M', 'S',
     'M', 'S'],
    ['S', 'M',
     'S', 'M'],
    ['S', 'S',
     'M', 'M'],
]


def is_x(r, c):
    p = [g[r-1][c-1], g[r-1][c+1],
         g[r+1][c-1], g[r+1][c+1]]
    return p in patterns


ret = 0

for r in range(1, r_size-1):
    for c in range(1, c_size-1):
        if g[r][c] == 'A' and is_x(r, c):
            ret += 1

print(ret)



