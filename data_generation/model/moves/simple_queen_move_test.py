import unittest

from model.moves.board import Square
from model.moves import simple_rook_move, simple_bishop_move, simple_queen_move
from model.moves.simple_queen_move import SimpleQueenMove

class TestSimpleQueenMove(unittest.TestCase):
    def test_san(self):
        # given
        move = SimpleQueenMove(Square.E4, Square.H7)

        # when
        san = move.san()

        # then
        self.assertEqual(san, "Qe4h7")

    def test_san_with_takes(self):
        # given
        move = SimpleQueenMove(Square.E4, Square.E1, takes = True)

        # when
        san = move.san()

        # then
        self.assertEqual(san, "Qe4xe1")

    def test_full_text(self):
        # given
        move = SimpleQueenMove(Square.B7, Square.A8)

        # when
        full_texts = move.full_texts()

        # then
        self.assertIn("Dame b7 auf a8", full_texts)
        self.assertIn("Dame b7 a8", full_texts)

    def test_full_text_with_takes(self):
        # given
        move = SimpleQueenMove(Square.B7, Square.A8, takes = True)

        # when
        full_texts = move.full_texts()

        # then
        self.assertIn("Dame b7 schlägt auf a8", full_texts)
        self.assertIn("Dame b7 schlägt a8", full_texts)

    def test_all(self):
        # given
        moves = simple_queen_move.all()

        # when / then
        for move in moves:
            self.assertNotEqual(move.source_square, move.target_square)

    def test_all_contains_all_rook_moves(self):
        # given
        all_queen_moves = simple_queen_move.all()
        all_rook_moves = simple_rook_move.all()

        # when
        queen_tuples = [(m.source_square, m.target_square) for m in all_queen_moves]
        rook_tuples  = [(m.source_square, m.target_square) for m in all_rook_moves]

        # then
        for rook_tuple in rook_tuples:
            self.assertIn(rook_tuple, queen_tuples)

    def test_all_contains_all_bishop_moves(self):
        # given
        all_queen_moves = simple_queen_move.all()
        all_bishop_moves = simple_bishop_move.all()

        # when
        queen_tuples = [(m.source_square, m.target_square) for m in all_queen_moves]
        bishop_tuples  = [(m.source_square, m.target_square) for m in all_bishop_moves]

        # then
        for bishop_tuple in bishop_tuples:
            self.assertIn(bishop_tuple, queen_tuples)

if __name__ == "__main__":
    unittest.main()
