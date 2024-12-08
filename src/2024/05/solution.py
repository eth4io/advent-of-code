import collections
import os
import re
from enum import Enum
from collections import Counter
from collections import defaultdict

dir = '2024/05'

input_file = 'input.txt'
# input_file = 'test_input.txt'
input_file_update = 'input_update.txt'
# input_file_update = 'test_input_update.txt'

file_path = os.path.join(dir, input_file)

edges = []

with open(os.path.join(dir, input_file), 'r') as file:
    edges = [line.strip().split('|') for line in file]

with open(os.path.join(dir, input_file_update), 'r') as file:
    updates = [line.strip().split(',') for line in file]


allowed = defaultdict(set)
denied = defaultdict(set)

for src, dst in edges:
    allowed[src].add(dst)
    denied[dst].add(src)

# part 1

def is_valid(update):
    for i in range(len(update)):
        for j in range(i+1, len(update)):
            if update[j] in denied[update[i]]:
                return False
    return True


ret = 0
for update in updates:
    if is_valid(update):
        mid = int(update[len(update) // 2])
        print(mid)
        ret += mid

print(ret)


# part 2

def topo_sort(order):
    ingress = Counter()
    g = defaultdict(list)

    for source, dest in edges:
        if source not in order or dest not in order:
            continue
        g[source].append(dest)
        ingress[dest] += 1
        if source not in ingress:
            ingress[source] = 0
        if dest not in ingress:
            ingress[dest] = 0

    queue = [dest for dest in ingress if ingress[dest] == 0]

    fixed = []
    for x in queue:
        fixed.append(x)

        for next in g[x]:
            ingress[next] -= 1
            if ingress[next] == 0:
                queue.append(next)

    return fixed

ret = 0
for update in updates:
    if not is_valid(update):
        fixed_update = topo_sort(update)
        mid = int(fixed_update[len(fixed_update) // 2])
        ret += mid

print(ret)
