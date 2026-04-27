import unittest

from model.moves import all_moves

class AllMovesTest(unittest.TestCase):
    def test_all_moves_have_the_required_fields(self):
        # given
        required_attributes = ['piece', 'source_file', 'source_rank', 'target_file', 'target_rank', 'capture',
                               'promoted_to']

        # when/then
        for move in all_moves.all():
            for attribute in required_attributes:
                self.assertTrue(hasattr(move, attribute), f"{attribute} is missing on move {move}")

if __name__ == "__main__":
    unittest.main()
