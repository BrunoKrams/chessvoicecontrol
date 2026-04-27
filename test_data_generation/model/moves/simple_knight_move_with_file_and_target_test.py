import unittest

from model.moves.board import Square, File
from model.moves import simple_knight_move_with_file_and_target
from model.moves.simple_knight_move_with_file_and_target import SimpleKnightMoveWithFileAndTarget


class TestSimpleKnightMoveWithFileAndTargetTest(unittest.TestCase):
    def test_san(self):
        # given
        move = SimpleKnightMoveWithFileAndTarget(Square.F2, Square.E4)

        # when
        san = move.san()

        # then
        self.assertEqual(san, "Nf2e4")

    def test_san_with_takes(self):
        # given
        move = SimpleKnightMoveWithFileAndTarget(Square.E4, Square.C5, capture=True)

        # when
        san = move.san()

        # then
        self.assertEqual(san, "Ne4xc5")

    def test_full_text(self):
        # given
        move = SimpleKnightMoveWithFileAndTarget(File.B, Square.C5)

        # when
        full_texts = move.full_texts()

        # then
        self.assertIn("Springer b auf c5", full_texts)
        self.assertIn("Springer b c5", full_texts)
        self.assertIn("Springer auf der b-Linie auf c5", full_texts)
        self.assertIn( "Springer auf der b-Linie c5", full_texts)
        self.assertIn("Der b-Springer auf c5", full_texts)
        self.assertIn("Der b-Springer c5", full_texts)
        self.assertIn( "Der Springer auf der b-Linie auf c5", full_texts)
        self.assertIn("Der Springer auf der b-Linie c5", full_texts)

    def test_full_text_with_takes(self):
        # given
        move = SimpleKnightMoveWithFileAndTarget(File.B, Square.C5, capture=True)

        # when
        full_texts = move.full_texts()

        # then
        self.assertIn("Springer b schlägt auf c5", full_texts)
        self.assertIn("Springer b schlägt c5", full_texts)
        self.assertIn("Springer auf der b-Linie schlägt auf c5", full_texts)
        self.assertIn("Springer auf der b-Linie schlägt c5", full_texts)
        self.assertIn("Der b-Springer schlägt auf c5", full_texts)
        self.assertIn("Der b-Springer schlägt c5", full_texts)
        self.assertIn("Der Springer auf der b-Linie schlägt auf c5", full_texts)
        self.assertIn("Der Springer auf der b-Linie schlägt c5", full_texts)

    def test_all(self):
        # given
        moves = simple_knight_move_with_file_and_target.all()

        # then
        self.assertIn(SimpleKnightMoveWithFileAndTarget(File.B, Square.C5, capture=True), moves)
        self.assertIn(SimpleKnightMoveWithFileAndTarget(File.B, Square.D6), moves)
        self.assertIn(SimpleKnightMoveWithFileAndTarget(File.B, Square.D6), moves)
        self.assertIn(SimpleKnightMoveWithFileAndTarget(File.F, Square.E4), moves)
        self.assertIn(SimpleKnightMoveWithFileAndTarget(File.E, Square.C5, capture=True), moves)

if __name__ == "__main__":
    unittest.main()
