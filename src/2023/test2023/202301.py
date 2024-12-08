import os

input_file = 'input.txt'
# input_file = 'test_input.txt'
dir = 'test2023'

file_path = os.path.join(dir, input_file)


with open(file_path, 'r') as file:
    # Read and process each line, stripping whitespace
    lines = [line.strip() for line in file]
# Output the list of lines

sum = 0


def cal(line: str) -> int:
    for c in line:
        if c.isdigit():
            l = int(c)
            break
    for c in range(len(line)-1, -1, -1):
        if line[c].isdigit():
            r = int(line[c])
            break
    return l*10 + r


for line in lines:
    sum += cal(line)
