import collections
import os

input_file = 'input.txt'
# input_file = 'test_input.txt'
dir = '2024/01'

file_path = os.path.join(dir, input_file)


with open(file_path, 'r') as file:
    # Read and process each line, stripping whitespace
    lines = [line.strip().split('   ') for line in file]

# part 1
lefts = [int(item[0]) for item in lines]
rights = [int(item[1]) for item in lines]

left_sorted = sorted(lefts)
right_sorted = sorted(rights)

sum = 0
for i in range(1000):
    sum += abs(left_sorted[i] - right_sorted[i])


# part 2


ret = 0
right_counter = collections.Counter(right_sorted)

for l in lefts:
    ret += l * right_counter[l]

print(ret)