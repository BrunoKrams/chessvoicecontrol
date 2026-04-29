import unittest
from test_data_generation.model.moves.board import File
from test_data_generation.model.moves.pawn_takes_with_file_and_promotion import PawnTakesWithFileAndPromotion
from test_data_generation.model.moves.pieces import Piece

class PawnTakesWithFileAndPromotionTest(unittest.TestCase):
    def test_san_queen_promotion(self):
        # given
        move = PawnTakesWithFileAndPromotion(File.E, File.F, Piece.QUEEN)

        # when
        san = move.san()

        # then
        self.assertEqual(san, "e7xf8=Q")

    def test_san_knight_promotion(self):
        # given
        move = PawnTakesWithFileAndPromotion(File.C, File.B, Piece.KNIGHT)

        # when
        san = move.san()

        # then
        self.assertEqual(san, "c7xb8=N")

    def test_full_texts_queen_promotion(self):
        # given
        move = PawnTakesWithFileAndPromotion(File.A, File.B, Piece.QUEEN)

        # when
        full_texts = move.full_texts()

        # then
        self.assertIn("Bauer a schlägt auf b8, Umwandlung zur Dame", full_texts)
        self.assertIn("Bauer a schlägt auf b8, Umwandlung Dame", full_texts)
        self.assertIn("Bauer a schlägt auf b8, Dame", full_texts)
        self.assertIn("a-Bauer schlägt auf b8, Umwandlung zur Dame", full_texts)
        self.assertIn("a-Bauer schlägt auf b8, Umwandlung Dame", full_texts)
        self.assertIn("a-Bauer schlägt auf b8, Dame", full_texts)
        self.assertIn("Der a-Bauer schlägt auf b8, Umwandlung zur Dame", full_texts)
        self.assertIn("Der a-Bauer schlägt auf b8, Umwandlung Dame", full_texts)
        self.assertIn("Der a-Bauer schlägt auf b8, Dame", full_texts)
        self.assertIn("a schlägt auf b8, Umwandlung zur Dame", full_texts)
        self.assertIn("a schlägt auf b8, Umwandlung Dame", full_texts)
        self.assertIn("a schlägt auf b8, Dame", full_texts)
        self.assertIn("a schlägt auf b8, Umwandlung zur Dame", full_texts)
        self.assertIn("a schlägt auf b8, Umwandlung Dame", full_texts)
        self.assertIn("a schlägt auf b8, Dame", full_texts)

    def test_full_texts_knight_promotion(self):
        # given
        move = PawnTakesWithFileAndPromotion(File.A, File.B, Piece.KNIGHT)

        # when
        full_texts = move.full_texts()

        # then
        self.assertIn("Bauer a schlägt auf b8, Umwandlung zum Springer", full_texts)
        self.assertIn("Bauer a schlägt auf b8, Umwandlung Springer", full_texts)
        self.assertIn("Bauer a schlägt auf b8, Springer", full_texts)
        self.assertIn("a-Bauer schlägt auf b8, Umwandlung zum Springer", full_texts)
        self.assertIn("a-Bauer schlägt auf b8, Umwandlung Springer", full_texts)
        self.assertIn("a-Bauer schlägt auf b8, Springer", full_texts)
        self.assertIn("Der a-Bauer schlägt auf b8, Umwandlung zum Springer", full_texts)
        self.assertIn("Der a-Bauer schlägt auf b8, Umwandlung Springer", full_texts)
        self.assertIn("Der a-Bauer schlägt auf b8, Springer", full_texts)
        self.assertIn("a schlägt auf b8, Umwandlung zum Springer", full_texts)
        self.assertIn("a schlägt auf b8, Umwandlung Springer", full_texts)
        self.assertIn("a schlägt auf b8, Springer", full_texts)
        self.assertIn("a schlägt auf b8, Umwandlung zum Springer", full_texts)
        self.assertIn("a schlägt auf b8, Umwandlung Springer", full_texts)
        self.assertIn("a schlägt auf b8, Springer", full_texts)

    def test_constructor_allows_only_promotable_pieces(self):
        for piece in [Piece.PAWN, Piece.KING]:
            with self.assertRaises(ValueError):
                PawnTakesWithFileAndPromotion(File.A, File.B, piece)

if __name__ == "__main__":
    unittest.main()

