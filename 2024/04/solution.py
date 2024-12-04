import collections
import os
import re
from enum import Enum

input_file = 'input.txt'
# input_file = 'test_input.txt'
dir = '2024/04'

file_path = os.path.join(dir, input_file)


with open(file_path, 'r') as file:
    # Read and process each line, stripping whitespace
    g = [line.strip() for line in file]


# part 1
r_size = len(g)
c_size = len(g[0])

END = '__END__'

dic = {
    'X': 'M',
    'M': 'A',
    'A': 'S',
    'S': END
}

# (row, col)
class Direction(Enum):
    UP = [-1, 0]
    DOWN = [1, 0]
    LEFT = [0, -1]
    RIGHT = [0, 1]
    UP_LEFT = [-1, -1]
    UP_RIGHT = [-1, 1]
    DOWN_LEFT = [1, -1]
    DOWN_RIGHT = [1, 1]


def check(r, c, d, cur_char) -> bool:
    if cur_char == END:
        return True

    r_diff, c_diff = d.value
    new_r = r + r_diff
    new_c = c + c_diff
    if new_r < 0 or new_r >= r_size or new_c < 0 or new_c >= c_size:
        return False
    if g[new_r][new_c] == cur_char:
        return check(new_r, new_c, d, dic[cur_char])


def get_xmas(r, c) -> int:
    sum = 0
    if g[r][c] == 'X':
        for d in Direction:
            if check(r, c, d, dic['X']):
                sum += 1

    return sum


ret = 0
for r in range(r_size):
    for c in range(c_size):
        ret += get_xmas(r, c)

print(ret)




# part 2
