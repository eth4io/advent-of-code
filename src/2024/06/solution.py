import collections
import os
import re
from enum import Enum
from collections import Counter
from collections import defaultdict

dir = '2024/06'

input_file = 'input.txt'
# input_file = 'test_input.txt'

edges = []

with open(os.path.join(dir, input_file), 'r') as file:
    lines = [line.strip() for line in file]

class Direction(Enum):
    UP = [-1, 0]
    DOWN = [1, 0]
    LEFT = [0, -1]
    RIGHT = [0, 1]

next_dir = {
    Direction.UP: Direction.RIGHT,
    Direction.RIGHT: Direction.DOWN,
    Direction.DOWN: Direction.LEFT,
    Direction.LEFT: Direction.UP
}

def init(lines):
    g = []
    for r_i, line in enumerate(lines):
        row = []
        for c_i in range(len(line)):
            row.append(line[c_i])
            if line[c_i] == '^':
                init_r = r_i
                init_c = c_i
        g.append(row)
    return g, [init_r, init_c]


def get_next(cur_r, cur_c, dir):
    return [cur_r + dir.value[0], cur_c + dir.value[1]]

def inbound(r, c):
    return r >= 0 and r < len(lines)  and c >= 0 and c < len(lines[r])

# part 1
def get_route(g, cur_r, cur_c):
    dir = Direction.UP
    guard_route = set()

    while True:
        guard_route.add((cur_r, cur_c))
        next_r, next_c = get_next(cur_r, cur_c, dir)
        if not inbound(next_r, next_c):
            break

        if g[next_r][next_c] == '#':
            dir = next_dir[dir]
        else:
            cur_r = next_r
            cur_c = next_c
    return guard_route

g, [cur_r, cur_c] = init(lines)
route = get_route(g, cur_r, cur_c)

print(len(route))

# part 2
def is_paradox(g, cur_r, cur_c):
    dir = Direction.UP
    visited = defaultdict(set)

    while True:
        if dir in visited[(cur_r, cur_c)]:
            return True
        visited[(cur_r, cur_c)].add(dir)
        next_r, next_c = get_next(cur_r, cur_c, dir)
        if not inbound(next_r, next_c):
            return False

        if g[next_r][next_c] == '#':
            dir = next_dir[dir]
        else:
            cur_r = next_r
            cur_c = next_c


g, [cur_r, cur_c] = init(lines)
r_n = len(lines)
c_n = len(lines[0])
ret = 0

route = get_route(g, cur_r, cur_c)
for r, c in route:
    g, [cur_r, cur_c] = init(lines)
    if g[r][c] != '^' and g[r][c] != '#':
        g[r][c] = '#'

    if is_paradox(g, cur_r, cur_c):
        print(ret, len(route))
        ret += 1
    else:
        print(ret, len(route))

print(ret)


