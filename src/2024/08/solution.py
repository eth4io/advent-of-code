from src.common.utils import *

class Day(Solution):

    def setup(self):
        self.g = Grid(self.input_lines)


    def get_antennas(self, g: Grid):
        antennas = defaultdict(set)
        for y in range(g.y_n):
            for x in range(g.x_n):
                char = g.get(y, x)
                if char != '.':
                    antennas[char].add((y, x))

        return antennas


    def get_antinode(self, a: (int, int), b: (int, int)) -> tuple[int, int]:
        xa, ya = a
        xb, yb = b
        return xb - xa + xb, yb - ya + yb


    def get_antinodes(self, a: (int, int), b: (int, int)) -> list[(int, int)]:
        antinodes = set()
        p0 = a
        p1 = b
        next = self.get_antinode(p0, p1)
        while self.g.is_in_range(next):
            antinodes.add(next)
            p0 = p1
            p1 = next
            next = self.get_antinode(p0, p1)

        return antinodes


    def part_1(self):
        antennas = self.get_antennas(self.g)
        antitodes = set()
        for key in antennas.keys():
            pairs = list(combinations(antennas[key], 2))
            for a, b in pairs:
                antinode = self.get_antinode(a, b)
                if self.g.is_in_range(antinode):
                    antitodes.add(antinode)
                antinode = self.get_antinode(b, a)
                if self.g.is_in_range(antinode):
                    antitodes.add(antinode)

        return len(antitodes)


    def part_2(self):
        antennas = self.get_antennas(self.g)
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



# setup
test_input_file, input_file = 'test_input.txt', 'input.txt'
test, real = Day(__file__, test_input_file), Day(__file__, input_file)

# part 1
print(colourify(Colour.LIGHT_BLUE, '------- part 1 -------'))
assert_equal(lambda: test.part_1(), 14, 'test')
assert_equal(lambda: real.part_1(), 299, 'real')

print()
# part 2
print(colourify(Colour.LIGHT_BLUE, '------- part 2 -------'))
assert_equal(lambda: test.part_2(), 34, 'test')
assert_equal(lambda: real.part_2(), 1032, 'real')

