from common.utils import *

class Day(Solution):
    r_n: int
    c_n: int

    def setup(self):
        self.r_n = len(self.input_lines)
        self.c_n = len(self.input_lines[0])


    def get_antennas(self, lines: str):
        antennas = defaultdict(set)
        for r in range(len(lines)):
            for c in range(len(lines[r])):
                char = lines[r][c]
                if char != '.':
                    antennas[char].add((r, c))

        return antennas


    def is_in_range(self, coord: (int, int)):
        r, c = coord
        return r >= 0 and r < self.r_n and c >= 0 and c < self.c_n


    def get_antinode(self, a: (int, int), b: (int, int)) -> (int, int):
        xa, ya = a
        xb, yb = b
        return xb - xa + xb, yb - ya + yb


    def get_antinodes(self, a: (int, int), b: (int, int)) -> list[(int, int)]:
        antinodes = set()
        p0 = a
        p1 = b
        next = self.get_antinode(p0, p1)
        while self.is_in_range(next):
            antinodes.add(next)
            p0 = p1
            p1 = next
            next = self.get_antinode(p0, p1)

        return antinodes


    def part_1(self):
        lines = self.input_lines

        antennas = self.get_antennas(lines)
        antitodes = set()
        for key in antennas.keys():
            pairs = list(combinations(antennas[key], 2))
            for a, b in pairs:
                antinode = self.get_antinode(a, b)
                if self.is_in_range(antinode):
                    antitodes.add(antinode)
                antinode = self.get_antinode(b, a)
                if self.is_in_range(antinode):
                    antitodes.add(antinode)

        return len(antitodes)


    def part_2(self):
        lines = self.input_lines

        antennas = self.get_antennas(lines)
        ret = set()
        for key in antennas.keys():
            ret = ret.union(antennas[key])
            pairs = list(combinations(antennas[key], 2))
            for a, b in pairs:
                antinodes = self.get_antinodes(a, b)
                ret = ret.union(antinodes)
                antinodes = self.get_antinodes(b, a)
                ret = ret.union(antinodes)

        return len(ret)


test_input_file = 'test_input.txt'
input_file = 'input.txt'
test_part_1_expected = 14
test_part_2_expected = 34

solve(day=Day, script_path=__file__,
      test_input_file=test_input_file, input_file=input_file,
      test_part_1_expected=test_part_1_expected, test_part_2_expected=test_part_2_expected,
      )
