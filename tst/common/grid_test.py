import unittest
from src.common.grid import Grid, Direction, DIRECTIONS_4, DIRECTIONS_8

class TestDirectionAndGrid(unittest.TestCase):

    def setUp(self):
        self.lines = ["aaaa", "bbbb", "cccc"]
        self.grid = Grid(self.lines)

    def test_direction_enum(self):
        # Test values of DIRECTIONS_4
        expected_directions_4 = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        self.assertEqual([d.value for d in DIRECTIONS_4], expected_directions_4)

        # Test values of DIRECTIONS_8
        expected_directions_8 = [
            [-1, 0], [-1, 1], [0, 1], [1, 1],
            [1, 0], [1, -1], [0, -1], [-1, -1]
        ]
        self.assertEqual([d.value for d in DIRECTIONS_8], expected_directions_8)

    def test_grid_initialization(self):
        # Test grid content
        expected_grid = [
            ['a', 'a', 'a', 'a'],
            ['b', 'b', 'b', 'b'],
            ['c', 'c', 'c', 'c']
        ]
        self.assertEqual(self.grid.grid, expected_grid)

        # Test row and column counts
        self.assertEqual(self.grid.y_n, 3)
        self.assertEqual(self.grid.x_n, 4)

    def test_get(self):
        # Test valid indices
        self.assertEqual(self.grid.get(0, 0), 'a')
        self.assertEqual(self.grid.get(2, 3), 'c')

        # Test invalid indices
        with self.assertRaises(IndexError):
            self.grid.get(3, 0)
        with self.assertRaises(IndexError):
            self.grid.get(0, 4)

    def test_get_moved(self):
        start_coordinates = (1, 1)  # 'b' at grid[1][1]

        self.assertEqual(Grid.get_moved(Direction.UP, start_coordinates), (0, 1))
        self.assertEqual(Grid.get_moved(Direction.DOWN, start_coordinates), (2, 1))
        self.assertEqual(Grid.get_moved(Direction.LEFT, start_coordinates), (1, 0))
        self.assertEqual(Grid.get_moved(Direction.RIGHT, start_coordinates), (1, 2))
        self.assertEqual(Grid.get_moved(Direction.UP_LEFT, start_coordinates), (0, 0))

    def test_is_in_range(self):
        # Test with valid coordinates
        self.assertTrue(self.grid.is_in_range((0, 0)))
        self.assertTrue(self.grid.is_in_range((2, 3)))

        # Test with invalid coordinates
        self.assertFalse(self.grid.is_in_range((3, 0)))
        self.assertFalse(self.grid.is_in_range((0, 4)))

        # Test overload with list
        self.assertTrue(self.grid.is_in_range([1, 1]))
        self.assertFalse(self.grid.is_in_range([3, 0]))

        # Test overload with separate integers
        self.assertTrue(self.grid.is_in_range(1, 1))
        self.assertFalse(self.grid.is_in_range(3, 0))

if __name__ == "__main__":
    unittest.main()

