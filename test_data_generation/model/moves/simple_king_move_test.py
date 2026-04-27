import unittest

from model.moves.board import Square
from model.moves import simple_king_move
from model.moves.simple_king_move import SimpleKingMove


class TestSimpleKingMove(unittest.TestCase):
    def test_san(self):
        # given
        move = SimpleKingMove(Square.F2, Square.G3)

        # when
        san = move.san()

        # then
        self.assertEqual(san, "Kf2g3")

    def test_san_with_takes(self):
        # given
        move = SimpleKingMove(Square.F2, Square.E3, capture=True)

        # when
        san = move.san()

        # then
        self.assertEqual(san, "Kf2xe3")

    def test_full_text(self):
        # given
        move = SimpleKingMove(Square.E4, Square.C5)

        # when
        full_texts = move.full_texts()

        # then
        self.assertIn("König e4 auf c5", full_texts)
        self.assertIn("König e4 c5", full_texts)

    def test_full_text_with_takes(self):
        # given
        move = SimpleKingMove(Square.B7, Square.C6, capture=True)

        # when
        full_texts = move.full_texts()

        # then
        self.assertIn("König b7 schlägt auf c6", full_texts)
        self.assertIn("König b7 schlägt c6", full_texts)

    def test_all(self):
        # given
        moves = simple_king_move.all()

        # then
        self.assertIn(SimpleKingMove(Square.B7, Square.C6, capture=True), moves)
        self.assertIn(SimpleKingMove(Square.B7, Square.B6), moves)
        self.assertIn(SimpleKingMove(Square.B7, Square.B8), moves)
        self.assertIn(SimpleKingMove(Square.F2, Square.E3), moves)
        self.assertIn(SimpleKingMove(Square.E4, Square.D5, capture=True), moves)


if __name__ == "__main__":
    unittest.main()
