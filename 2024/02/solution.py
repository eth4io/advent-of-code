import collections
import os

input_file = 'input.txt'
# input_file = 'test_input.txt'
dir = '2024/02'

file_path = os.path.join(dir, input_file)


with open(file_path, 'r') as file:
    # Read and process each line, stripping whitespace
    lines = [line.strip().split(' ') for line in file]


def calc(nums) -> bool:
    asc = nums[0] < nums[1]
    if asc:
        for i in range(0, len(nums) - 1):
            if nums[i] >= nums[i + 1] or abs(nums[i] - nums[i + 1]) > 3:
                return False
    else:
        for i in range(0, len(nums) - 1):
            if nums[i] <= nums[i + 1] or abs(nums[i] - nums[i + 1]) > 3:
                return False
    return True

def calc_dampen(nums) -> bool:
    if calc(nums):
        # print(nums, "pass")
        return True
    else:
        for i in range(len(nums)):
            if calc(nums[:i] + nums[i+1:]):
                print(nums, "*pass")
                return True
        print(nums, "fail")
        return False


ret = len(lines)
for line in lines:
    nums = [int(item) for item in line]
    if not calc_dampen(nums):
        ret -= 1

print(ret)
