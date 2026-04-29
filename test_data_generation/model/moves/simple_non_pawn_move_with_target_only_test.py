import unittest

from test_data_generation.model.moves.board import Square
from test_data_generation.model.moves import simple_non_pawn_move_with_target_only
from test_data_generation.model.moves.simple_non_pawn_move_with_target_only import SimpleNonPawnMoveWithTargetOnly
from test_data_generation.model.moves.pieces import Piece


class SimpleNonPawnMoveWithTargetOnlyTest(unittest.TestCase):
    def test_san(self):
        # given
        move = SimpleNonPawnMoveWithTargetOnly(Piece.KNIGHT, Square.E4)

        # when
        san = move.san()

        # then
        self.assertEqual(san, "Ne4")

    def test_san_with_takes(self):
        # given
        move = SimpleNonPawnMoveWithTargetOnly(Piece.KING, Square.E4, capture=True)

        # when
        san = move.san()

        # then
        self.assertEqual(san, "Kxe4")

    def test_full_text(self):
        # given
        move = SimpleNonPawnMoveWithTargetOnly(Piece.ROOK, Square.D6)

        # when
        full_texts = move.full_texts()

        # then
        self.assertIn("Turm d6", full_texts)
        self.assertIn("Turm d6", full_texts)

    def test_full_text_with_takes(self):
        # given
        move = SimpleNonPawnMoveWithTargetOnly(Piece.KNIGHT, Square.C5, capture=True)

        # when
        full_texts = move.full_texts()

        # then
        self.assertIn("Springer schlägt auf c5", full_texts)
        self.assertIn("Springer schlägt c5", full_texts)

    def test_all(self):
        # given
        moves = simple_non_pawn_move_with_target_only.all()

        # then
        self.assertIn(SimpleNonPawnMoveWithTargetOnly(Piece.KNIGHT, Square.C5, capture=True), moves)
        self.assertIn(SimpleNonPawnMoveWithTargetOnly(Piece.BISHOP, Square.D6), moves)
        self.assertIn(SimpleNonPawnMoveWithTargetOnly(Piece.ROOK, Square.D6), moves)
        self.assertIn(SimpleNonPawnMoveWithTargetOnly(Piece.QUEEN, Square.E4), moves)
        self.assertIn(SimpleNonPawnMoveWithTargetOnly(Piece.KING, Square.C5, capture=True), moves)


if __name__ == "__main__":
    unittest.main()
