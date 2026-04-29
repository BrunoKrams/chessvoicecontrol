import unittest

from test_data_generation.model.moves.board import Square
from test_data_generation.model.moves.simple_pawn_move import SimplePawnMove


class TestSimplePawnMoveSan(unittest.TestCase):
    def test_san(self):
        # given
        move = SimplePawnMove(Square.E4)

        # when
        san = move.san()

        # then
        self.assertEqual(san, "e4")

    def test_full_text(self):
        # given
        move = SimplePawnMove(Square.B7)

        # when
        full_texts = move.full_texts()

        # then
        self.assertIn("b7", full_texts)
        self.assertIn("Bauer auf b7", full_texts)
        self.assertIn("Bauer b7", full_texts)

if __name__ == "__main__":
    unittest.main()
