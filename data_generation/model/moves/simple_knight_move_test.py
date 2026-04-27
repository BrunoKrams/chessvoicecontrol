import unittest

from model.moves.board import Square
from model.moves import simple_knight_move
from model.moves.simple_knight_move import SimpleKnightMove


class TestSimpleKnightMove(unittest.TestCase):
    def test_san(self):
        # given
        move = SimpleKnightMove(Square.F2, Square.E4)

        # when
        san = move.san()

        # then
        self.assertEqual(san, "Nf2e4")

    def test_san_with_takes(self):
        # given
        move = SimpleKnightMove(Square.E4, Square.C5, capture=True)

        # when
        san = move.san()

        # then
        self.assertEqual(san, "Ne4xc5")

    def test_full_text(self):
        # given
        move = SimpleKnightMove(Square.B7, Square.D6)

        # when
        full_texts = move.full_texts()

        # then
        self.assertIn("Springer b7 auf d6", full_texts)
        self.assertIn("Springer b7 d6", full_texts)

    def test_full_text_with_takes(self):
        # given
        move = SimpleKnightMove(Square.B7, Square.C5, capture=True)

        # when
        full_texts = move.full_texts()

        # then
        self.assertIn("Springer b7 schlägt auf c5", full_texts)
        self.assertIn("Springer b7 schlägt c5", full_texts)

    def test_all(self):
        # given
        moves = simple_knight_move.all()

        # then
        self.assertIn(SimpleKnightMove(Square.B7, Square.C5, capture=True), moves)
        self.assertIn(SimpleKnightMove(Square.B7, Square.D6), moves)
        self.assertIn(SimpleKnightMove(Square.B7, Square.D6), moves)
        self.assertIn(SimpleKnightMove(Square.F2, Square.E4), moves)
        self.assertIn(SimpleKnightMove(Square.E4, Square.C5, capture=True), moves)


if __name__ == "__main__":
    unittest.main()
