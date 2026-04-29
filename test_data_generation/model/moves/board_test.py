import unittest
from collections import defaultdict

from test_data_generation.model.moves import board
from test_data_generation.model.moves.board import Square, Diagonal, Rank, File, get_rank, get_file, get_square


class BoardTest(unittest.TestCase):

    def test_each_non_corner_boundary_field_occurs_exactly_twice_in_the_diagonals(self):
        # when
        counts = defaultdict(int)
        for diagonal in list(board.Diagonal):
            counts[diagonal.name.split("_")[0]] += 1
            counts[diagonal.name.split("_")[1]] += 1

        # then
        for square, count in counts.items():
            if not square in ["A1", "A8", "H1", "H8"]:
                self.assertEqual(count, 2, f"{square} appears {count} times, expected 2")

    def test_each_corner_field_occurs_exactly_once_in_the_diagonals(self):
        # when
        counts = defaultdict(int)
        for diagonal in list(board.Diagonal):
            counts[diagonal.name.split("_")[0]] += 1
            counts[diagonal.name.split("_")[1]] += 1

        # then
        for square, count in counts.items():
            if square in ["A1", "A8", "H1", "H8"]:
                self.assertEqual(count, 1, f"{square} appears {count} times, expected 1")

    def test_get_diagonals(self):
        # given
        square = Square.B7

        # when
        result = board.get_diagonals(square)

        # then
        self.assertCountEqual(result, [Diagonal.H1_A8, Diagonal.A6_C8])

    def test_get_diagonals_for_corner_field(self):
        # given
        square = Square.H8

        # when
        result = board.get_diagonals(square)

        # then
        self.assertEqual(result, [Diagonal.A1_H8])

    def test_get_rank(self):
        # given
        square = Square.B7

        # when
        result = board.get_rank(square)

        # then
        self.assertEqual(result, Rank.SEVENTH)

    def test_get_file(self):
        # given
        square = Square.G3

        # when
        result = board.get_file(square)

        # then
        self.assertEqual(result, File.G)

    def test_each_square_has_a_rank(self):
        # given
        all_squares = list(Square)

        # when / then
        for square in all_squares:
            self.assertIsNotNone(get_rank(square))

    def test_each_square_has_a_file(self):
        # given
        all_squares = list(Square)

        # when / then
        for square in all_squares:
            self.assertIsNotNone(get_file(square))

    def test_get_square(self):
        # given
        file = File.G
        rank = Rank.SEVENTH

        # when
        square = get_square(file, rank)

        # then
        self.assertEqual(square, Square.G7)

    def test_rank_arithmetic(self):
        # given
        rank = Rank.SECOND

        # when
        result = rank + 3

        # then
        self.assertEqual(result, Rank.FIFTH)

    def test_rank_arithmetic_with_overflow(self):
        # given
        rank = Rank.SIXTH

        # when
        result = rank + 3

        # then
        self.assertIsNone(result)

    def test_file_arithmetic(self):
        # given
        file = File.E

        # when
        result = file - 2

        # then
        self.assertEqual(result, File.C)

    def test_file_arithmetic_with_overflow(self):
        # given
        file = File.F

        # when
        result = file + 3

        # then
        self.assertIsNone(result)


if __name__ == "__main__":
    unittest.main()
