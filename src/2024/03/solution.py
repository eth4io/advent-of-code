import collections
import os
import re

input_file = 'input.txt'
# input_file = 'test_input.txt'
dir = '2024/03'

file_path = os.path.join(dir, input_file)


with open(file_path, 'r') as file:
    # Read and process each line, stripping whitespace
    lines = [line for line in file]


# part 1

def match_mul(line) -> int:
    pattern = r"mul\(\d{1,3},\d{1,3}\)"

    sum = 0

    matches = re.findall(pattern, line)
    for match in matches:
        num1, num2 = match[4:-1].split(',')
        sum += int(num1) * int(num2)

    print(sum)
    return sum


# part 2

def calc(s) -> int:
    num1, num2 = s[4:-1].split(',')
    return int(num1) * int(num2)


regex_list = [
    r"mul\([0-9]{1,3},[0-9]{1,3}\)",
    r"do\(\)",
    r"don\'t\(\)"
]
rex = re.compile('|'.join(regex_list))

ret = 0
is_enabled = True
for line in lines:
    matches = rex.findall(line)
    for match in matches:
        if match == 'do()':
            is_enabled = True
        elif match == "don't()":
            is_enabled = False
        else:
            if is_enabled:
                ret += calc(match)

print(ret)
