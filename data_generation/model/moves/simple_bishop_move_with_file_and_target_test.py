import unittest

from model.moves.board import Square, File
from model.moves import simple_bishop_move_with_file_and_target
from model.moves.simple_bishop_move_with_file_and_target import SimpleBishopMoveWithFileAndTarget


class TestSimpleBishopMoveWithFileAndTargetTest(unittest.TestCase):
    def test_san(self):
        # given
        move = SimpleBishopMoveWithFileAndTarget(File.F, Square.D4)

        # when
        san = move.san()

        # then
        self.assertEqual(san, "Bfd4")

    def test_san_with_takes(self):
        # given
        move = SimpleBishopMoveWithFileAndTarget(File.E, Square.C5, takes=True)

        # when
        san = move.san()

        # then
        self.assertEqual(san, "Bexc5")

    def test_full_text(self):
        # given
        move = SimpleBishopMoveWithFileAndTarget(File.B, Square.C5)

        # when
        full_texts = move.full_texts()

        # then
        self.assertIn("Läufer b auf c5", full_texts)
        self.assertIn("Läufer b c5", full_texts)
        self.assertIn("Läufer auf der b-Linie auf c5", full_texts)
        self.assertIn("Läufer auf der b-Linie c5", full_texts)
        self.assertIn("Der b-Läufer auf c5", full_texts)
        self.assertIn("Der b-Läufer c5", full_texts)
        self.assertIn("Der Läufer auf der b-Linie auf c5", full_texts)
        self.assertIn("Der Läufer auf der b-Linie c5", full_texts)

    def test_full_text_with_takes(self):
        # given
        move = SimpleBishopMoveWithFileAndTarget(File.B, Square.C5, takes=True)

        # when
        full_texts = move.full_texts()

        # then
        self.assertIn("Läufer b schlägt auf c5", full_texts)
        self.assertIn("Läufer b schlägt c5", full_texts)
        self.assertIn("Läufer auf der b-Linie schlägt auf c5", full_texts)
        self.assertIn("Läufer auf der b-Linie schlägt c5", full_texts)
        self.assertIn("Der b-Läufer schlägt auf c5", full_texts)
        self.assertIn("Der b-Läufer schlägt c5", full_texts)
        self.assertIn("Der Läufer auf der b-Linie schlägt auf c5", full_texts)
        self.assertIn("Der Läufer auf der b-Linie schlägt c5", full_texts)

    def test_all(self):
        # given
        moves = simple_bishop_move_with_file_and_target.all()

        # then
        self.assertIn(SimpleBishopMoveWithFileAndTarget(File.B, Square.C5, takes=True), moves)
        self.assertIn(SimpleBishopMoveWithFileAndTarget(File.B, Square.D6), moves)
        self.assertIn(SimpleBishopMoveWithFileAndTarget(File.B, Square.D6), moves)
        self.assertIn(SimpleBishopMoveWithFileAndTarget(File.F, Square.E4), moves)
        self.assertIn(SimpleBishopMoveWithFileAndTarget(File.E, Square.C5, takes=True), moves)


if __name__ == "__main__":
    unittest.main()
