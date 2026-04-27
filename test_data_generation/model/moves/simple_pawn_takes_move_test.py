import unittest

from model.moves.board import Square
from model.moves.simple_pawn_takes_move import SimplePawnTakesMove


class TestSimplePawnTakesMove(unittest.TestCase):
    def test_san(self):
        # given
        move = SimplePawnTakesMove(Square.E4)

        # when
        san = move.san()

        # then
        self.assertEqual(san, "e4")

    def test_full_text(self):
        # given
        move = SimplePawnTakesMove(Square.B7)

        # when
        full_texts = move.full_texts()

        # then
        self.assertIn("Bauer schlägt auf b7", full_texts)
        self.assertIn("Bauer schlägt b7", full_texts)


if __name__ == "__main__":
    unittest.main()

