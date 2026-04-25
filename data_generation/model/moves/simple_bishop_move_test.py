import unittest

from model.moves.board import Square
from model.moves import simple_bishop_move
from model.moves.simple_bishop_move import SimpleBishopMove

class TestSimpleBishopMove(unittest.TestCase):
    def test_san(self):
        # given
        move = SimpleBishopMove(Square.E4, Square.H7)

        # when
        san = move.san()

        # then
        self.assertEqual(san, "Be4h7")

    def test_san_with_takes(self):
        # given
        move = SimpleBishopMove(Square.E4, Square.H7, takes = True)

        # when
        san = move.san()

        # then
        self.assertEqual(san, "Be4xh7")

    def test_full_text(self):
        # given
        move = SimpleBishopMove(Square.B7, Square.A8)

        # when
        full_texts = move.full_texts()

        # then
        self.assertIn("Läufer b7 auf a8", full_texts)
        self.assertIn("Läufer b7 a8", full_texts)

    def test_full_text_with_takes(self):
        # given
        move = SimpleBishopMove(Square.B7, Square.A8, takes = True)

        # when
        full_texts = move.full_texts()

        # then
        self.assertIn("Läufer b7 schlägt auf a8", full_texts)
        self.assertIn("Läufer b7 schlägt a8", full_texts)

    def test_all(self):
        # given
        moves = simple_bishop_move.all()

        # when / then
        for move in moves:
            self.assertNotEqual(move.source_square, move.target_square)

if __name__ == "__main__":
    unittest.main()
