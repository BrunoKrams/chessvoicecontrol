import unittest
from model.moves.board import File
from model.moves.pawn_takes_with_promotion import PawnTakesWithPromotion
from model.moves.pieces import Piece


class PawnTakesWithPromotionSan(unittest.TestCase):
    def test_san_queen_promotion(self):
        # given
        move = PawnTakesWithPromotion(File.E, Piece.QUEEN)

        # when
        san = move.san()

        # then
        self.assertEqual(san, "xe8=Q")

    def test_san_knight_promotion(self):
        # given
        move = PawnTakesWithPromotion(File.C,Piece.KNIGHT)

        # when
        san = move.san()

        # then
        self.assertEqual(san, "xc8=N")

    def test_full_texts_queen_promotion(self):
        # given
        move = PawnTakesWithPromotion(File.A, Piece.QUEEN)

        # when
        full_texts = move.full_texts()

        # then
        self.assertIn("Bauer schlägt auf a8, Umwandlung zur Dame", full_texts)
        self.assertIn("Bauer schlägt auf a8, Umwandlung Dame", full_texts)
        self.assertIn("Bauer schlägt auf a8, Dame", full_texts)

    def test_full_texts_knight_promotion(self):
        # given
        move = PawnTakesWithPromotion(File.C, Piece.KNIGHT)

        # when
        full_texts = move.full_texts()

        # then
        self.assertIn("Bauer schlägt auf c8, Umwandlung zum Springer", full_texts)
        self.assertIn("Bauer schlägt auf c8, Umwandlung Springer", full_texts)
        self.assertIn("Bauer schlägt auf c8, Springer", full_texts)

    def test_constructor_allows_only_promotable_pieces(self):
        for piece in [Piece.PAWN, Piece.KING]:
            with self.assertRaises(ValueError):
                PawnTakesWithPromotion(File.A, piece)

if __name__ == "__main__":
    unittest.main()

