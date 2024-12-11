import unittest
from src.common.grid import Grid, Direction, DIRECTIONS_4, DIRECTIONS_8, DIRECTIONS_DIAGONAL


class TestDirectionAndGrid(unittest.TestCase):

    def setUp(self):
        self.lines = ["1234", "5678", "9012"]
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

        # Test values of DIRECTIONS_DIAGONAL
        expected_diagonal = [[-1, 1], [1, 1], [1, -1], [-1, -1]]
        self.assertEqual([d.value for d in DIRECTIONS_DIAGONAL], expected_diagonal)

    def test_grid_initialization(self):
        # Test grid content
        expected_grid = [
            ['1', '2', '3', '4'],
            ['5', '6', '7', '8'],
            ['9', '0', '1', '2']
        ]
        self.assertEqual(self.grid.grid, expected_grid)

        # Test row and column counts
        self.assertEqual(self.grid.y_n, 3)
        self.assertEqual(self.grid.x_n, 4)

    def test_to_int(self):
        # Convert grid to integers
        self.grid.to_int()
        expected_grid = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 0, 1, 2]
        ]
        self.assertEqual(self.grid.grid, expected_grid)

    def test_build_cell_map(self):
        self.grid.build_cell_map()
        expected_map = {
            '1': [(0, 0), (2, 2)],
            '2': [(0, 1), (2, 3)],
            '3': [(0, 2)],
            '4': [(0, 3)],
            '5': [(1, 0)],
            '6': [(1, 1)],
            '7': [(1, 2)],
            '8': [(1, 3)],
            '9': [(2, 0)],
            '0': [(2, 1)],
        }
        self.assertEqual(self.grid.cell_map, expected_map)

    def test_get(self):
        # Test valid indices
        self.assertEqual(self.grid.get(0, 0), '1')
        self.assertEqual(self.grid.get((2, 3)), '2')

        # Test invalid indices
        with self.assertRaises(IndexError):
            self.grid.get(3, 0)
        with self.assertRaises(IndexError):
            self.grid.get(0, 4)

    def test_get_all_in_range_moved(self):
        # Test valid moves
        start_coordinates = (1, 1)
        directions = DIRECTIONS_4
        result = self.grid.get_all_in_range_moved(directions, start_coordinates)
        expected = [(0, 1), (1, 2), (2, 1), (1, 0)]
        self.assertEqual(result, expected)

        # Test invalid moves
        start_coordinates = (0, 0)
        directions = DIRECTIONS_8
        result = self.grid.get_all_in_range_moved(directions, start_coordinates)
        expected = [(0, 1), (1, 1), (1, 0)]
        self.assertEqual(result, expected)

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

    def test_str(self):
        # Test string representation of the grid
        expected_output = "1 2 3 4\n5 6 7 8\n9 0 1 2\n"
        self.assertEqual(str(self.grid), expected_output)


if __name__ == "__main__":
    unittest.main()
