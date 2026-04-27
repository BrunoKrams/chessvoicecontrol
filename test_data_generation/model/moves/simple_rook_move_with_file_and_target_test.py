import unittest

from model.moves.board import Square, File
from model.moves import simple_rook_move_with_file_and_target
from model.moves.simple_rook_move_with_file_and_target import SimpleRookMoveWithFileAndTarget


class TestSimpleRookMoveWithFileAndTargetTest(unittest.TestCase):
    def test_san(self):
        # given
        move = SimpleRookMoveWithFileAndTarget(File.F, Square.D4)

        # when
        san = move.san()

        # then
        self.assertEqual(san, "Rfd4")

    def test_san_with_takes(self):
        # given
        move = SimpleRookMoveWithFileAndTarget(File.E, Square.C5, capture=True)

        # when
        san = move.san()

        # then
        self.assertEqual(san, "Rexc5")

    def test_full_text(self):
        # given
        move = SimpleRookMoveWithFileAndTarget(File.B, Square.C5)

        # when
        full_texts = move.full_texts()

        # then
        self.assertIn("Turm b auf c5", full_texts)
        self.assertIn("Turm b c5", full_texts)
        self.assertIn("Turm auf der b-Linie auf c5", full_texts)
        self.assertIn("Turm auf der b-Linie c5", full_texts)
        self.assertIn("Der b-Turm auf c5", full_texts)
        self.assertIn("Der b-Turm c5", full_texts)
        self.assertIn("Der Turm auf der b-Linie auf c5", full_texts)
        self.assertIn("Der Turm auf der b-Linie c5", full_texts)

    def test_full_text_with_takes(self):
        # given
        move = SimpleRookMoveWithFileAndTarget(File.B, Square.C5, capture=True)

        # when
        full_texts = move.full_texts()

        # then
        self.assertIn("Turm b schlägt auf c5", full_texts)
        self.assertIn("Turm b schlägt c5", full_texts)
        self.assertIn("Turm auf der b-Linie schlägt auf c5", full_texts)
        self.assertIn("Turm auf der b-Linie schlägt c5", full_texts)
        self.assertIn("Der b-Turm schlägt auf c5", full_texts)
        self.assertIn("Der b-Turm schlägt c5", full_texts)
        self.assertIn("Der Turm auf der b-Linie schlägt auf c5", full_texts)
        self.assertIn("Der Turm auf der b-Linie schlägt c5", full_texts)

    def test_all(self):
        # given
        moves = simple_rook_move_with_file_and_target.all()

        # then
        self.assertIn(SimpleRookMoveWithFileAndTarget(File.B, Square.C5, capture=True), moves)
        self.assertIn(SimpleRookMoveWithFileAndTarget(File.B, Square.D6), moves)
        self.assertIn(SimpleRookMoveWithFileAndTarget(File.B, Square.D6), moves)
        self.assertIn(SimpleRookMoveWithFileAndTarget(File.F, Square.E4), moves)
        self.assertIn(SimpleRookMoveWithFileAndTarget(File.E, Square.C5, capture=True), moves)


if __name__ == "__main__":
    unittest.main()
