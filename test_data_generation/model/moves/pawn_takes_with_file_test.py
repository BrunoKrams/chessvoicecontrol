import unittest
from test_data_generation.model.moves.board import File, Square
from test_data_generation.model.moves.pawn_takes_with_file import PawnTakesMoveWithFile


class TestPawnTakesMoveWithFile(unittest.TestCase):
    def test_san(self):
        # given
        move = PawnTakesMoveWithFile(File.E, Square.D5)

        # when
        san = move.san()

        # then
        self.assertEqual(san, "exd5")

    def test_full_text(self):
        # given
        move = PawnTakesMoveWithFile(File.E, Square.F5)

        # when
        full_texts = move.full_texts()

        # then
        self.assertIn("e-Bauer schlägt auf f5", full_texts)
        self.assertIn("e-Bauer schlägt f5", full_texts)
        self.assertIn("Der e-Bauer schlägt auf f5", full_texts)
        self.assertIn("Der e-Bauer schlägt f5", full_texts)
        self.assertIn("e schlägt f5", full_texts)
        self.assertIn("e schlägt auf f5", full_texts)


if __name__ == "__main__":
    unittest.main()

