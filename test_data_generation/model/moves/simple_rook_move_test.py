import unittest

from test_data_generation.model.moves.board import Square
from test_data_generation.model.moves import simple_rook_move
from test_data_generation.model.moves.simple_rook_move import SimpleRookMove

class TestSimpleRookMove(unittest.TestCase):
    def test_san(self):
        # given
        move = SimpleRookMove(Square.E4, Square.E1)

        # when
        san = move.san()

        # then
        self.assertEqual(san, "Re4e1")

    def test_san_with_takes(self):
        # given
        move = SimpleRookMove(Square.E4, Square.E1, capture=True)

        # when
        san = move.san()

        # then
        self.assertEqual(san, "Re4xe1")

    def test_full_text(self):
        # given
        move = SimpleRookMove(Square.B7, Square.H7)

        # when
        full_texts = move.full_texts()

        # then
        self.assertIn("Turm b7 auf h7", full_texts)
        self.assertIn("Turm b7 h7", full_texts)

    def test_full_text_with_takes(self):
        # given
        move = SimpleRookMove(Square.B7, Square.H7, capture=True)

        # when
        full_texts = move.full_texts()

        # then
        self.assertIn("Turm b7 schlägt auf h7", full_texts)
        self.assertIn("Turm b7 schlägt h7", full_texts)

    def test_all(self):
        # given
        moves = simple_rook_move.all()

        # when / then
        for move in moves:
            self.assertNotEqual(move.source_square, move.target_square)

if __name__ == "__main__":
    unittest.main()
