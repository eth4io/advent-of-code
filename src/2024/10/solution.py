from src.common.utils import *


class Day(Solution):

  def setup(self):
    self.disk = [int(num) for num in self.input_lines[0]]
    self.EMPTY = None
    self.dict = SortedDict(int)
    self.empties = []


  def get_data(self, disk: list[int]):
    blocks = []
    cumulated_size = 0
    for i, size in enumerate(disk):
      data = i // 2
      is_data = i % 2 == 0
      if is_data:
        blocks += [data] * size
        self.dict[data] = (cumulated_size, size)
      else:
        blocks += [self.EMPTY] * size
        self.empties.append((cumulated_size, size))
      cumulated_size += size
    return blocks


  def get_compact(self, data: list[int]):
    c = 0
    tail_i = len(data) - 1
    for i, content in enumerate(data):
      if content == self.EMPTY:
        while data[tail_i] == self.EMPTY:
          tail_i -= 1
          c += 1
        data[i] = data[tail_i]
        tail_i -= 1

    return data[:tail_i+c+1]


  def get_first_sufficient_space(self, empties, size):
    for j, empty in enumerate(empties):
      e_i, e_size = empty
      if e_size >= size:
        return e_i, e_size, j

    return None, None, None


  def get_compact_whole_file(self, data) -> list[int]:
    for content in range(max([item for item in data if item is not None]), 0, -1):
      i, size = self.dict[content]
      e_i, e_size, e_j = self.get_first_sufficient_space(self.empties, size)
      if e_i is None or e_i > i:
        continue
      for j in range(size):
        data[i+j] = self.EMPTY
        data[e_i+j] = content
      if e_size == size:
        del self.empties[e_j]
      else:
        self.empties[e_j] = (e_i+size, e_size-size)

    return data


  def get_checksum(self, compact: list[int]) -> int:
    checksum = 0
    for i, content in enumerate(compact):
      if content == self.EMPTY:
        continue
      checksum += i * content

    return checksum


  def update_empties(self):
    i = 0
    while i + 1 < len(self.empties):
      cur = self.empties[i]
      next = self.empties[i+1]
      if cur[0] + cur[1] == next[0]:
        self.empties[i] = (cur[0], cur[1] + next[1])
        del self.empties[i+1]
      else:
        i += 1


  def part_1(self):
    data = self.get_data(self.disk)
    compact = self.get_compact(data)
    checksum = self.get_checksum(compact)
    return checksum


  def part_2(self):
    data = self.get_data(self.disk)
    compact = self.get_compact_whole_file(data)
    checksum = self.get_checksum(compact)
    return checksum


# test
test_input_file = 'test_input.txt'
test_part_1_expected = 1928
test_part_2_expected = 2858

# real
input_file = 'input.txt'
part_1_expected = 6421128769094
part_1_expected_false = [None]

part_2_expected = 6448168620520
part_2_expected_false = [None]

solve(day=Day, script_path=__file__,
      test_input_file=test_input_file, input_file=input_file,
      test_part_1_expected=test_part_1_expected, test_part_2_expected=test_part_2_expected,
      part_1_expected=part_1_expected, part_2_expected=part_2_expected,
      part_1_expected_false=part_1_expected_false, part_2_expected_false=part_2_expected_false,
      )



