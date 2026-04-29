import unittest
from test_data_generation.model.moves.board import File
from test_data_generation.model.moves.pieces import Piece
from test_data_generation.model.moves.simple_pawn_move_with_promotion import SimplePawnMoveWithPromotion


class TestSimplePawnMoveWithPromotionSan(unittest.TestCase):
    def test_san_queen_promotion(self):
        # given
        move = SimplePawnMoveWithPromotion(File.E, Piece.QUEEN)

        # when
        san = move.san()

        # then
        self.assertEqual(san, "e8=Q")

    def test_san_knight_promotion(self):
        # given
        move = SimplePawnMoveWithPromotion(File.A, Piece.KNIGHT)

        # when
        san = move.san()

        # then
        self.assertEqual(san, "a8=N")

    def test_full_texts_queen_promotion(self):
        # given
        move = SimplePawnMoveWithPromotion(File.A, Piece.QUEEN)

        # when
        full_texts = move.full_texts()

        # then
        self.assertIn("Bauer auf a8, Umwandlung zur Dame", full_texts)
        self.assertIn("Bauer auf a8, Umwandlung Dame", full_texts)
        self.assertIn("Bauer auf a8, Dame", full_texts)
        self.assertIn("a8, Umwandlung zur Dame", full_texts)
        self.assertIn("a8, Umwandlung Dame", full_texts)
        self.assertIn("a8, Dame", full_texts)

    def test_full_texts_knight_promotion(self):
        # given
        move = SimplePawnMoveWithPromotion(File.C, Piece.KNIGHT)

        # when
        full_texts = move.full_texts()

        # then
        self.assertIn("Bauer auf c8, Umwandlung zum Springer", full_texts)
        self.assertIn("Bauer auf c8, Umwandlung Springer", full_texts)
        self.assertIn("Bauer auf c8, Springer", full_texts)
        self.assertIn("c8, Umwandlung zum Springer", full_texts)
        self.assertIn("c8, Umwandlung Springer", full_texts)
        self.assertIn("c8, Springer", full_texts)

    def test_constructor_allows_only_promotable_pieces(self):
        for piece in [Piece.PAWN, Piece.KING]:
            with self.assertRaises(ValueError):
                SimplePawnMoveWithPromotion(File.A, piece)

if __name__ == "__main__":
    unittest.main()

