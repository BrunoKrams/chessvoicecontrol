import unittest

import torch

import transformer
from model.moves.board import Square
from model.moves.castling import CastleKingSide
from model.moves.pieces import Piece
from model.moves.simple_non_pawn_move import SimpleNonPawnMove
from model.moves.simple_pawn_move import SimplePawnMove


class TransformeTest(unittest.TestCase):
    def test_move_to_targets_pawn_move(self):
        # given
        move = SimplePawnMove(Square.B5)

        # when
        result = transformer.move_to_targets(move)

        # then
        self.assertEqual(result,
                         {
                             "type": torch.tensor(0, dtype=torch.long),
                             "piece": torch.tensor(1, dtype=torch.long),
                             "source_file": torch.tensor(2, dtype=torch.long),
                             "source_rank": torch.tensor(0, dtype=torch.long),
                             "target_file": torch.tensor(2, dtype=torch.long),
                             "target_rank": torch.tensor(5, dtype=torch.long),
                             "capture": torch.tensor(0, dtype=torch.long),
                             "promotion_piece": torch.tensor(0, dtype=torch.long)
                         })

    def test_move_to_targets_piece_move_with_capture(self):
        # given
        move = SimpleNonPawnMove(Piece.KNIGHT, Square.B5, Square.C3, capture=True)

        # when
        result = transformer.move_to_targets(move)

        # then
        self.assertEqual(result,
                         {
                             "type": torch.tensor(0, dtype=torch.long),
                             "piece": torch.tensor(2, dtype=torch.long),
                             "source_file": torch.tensor(2, dtype=torch.long),
                             "source_rank": torch.tensor(5, dtype=torch.long),
                             "target_file": torch.tensor(3, dtype=torch.long),
                             "target_rank": torch.tensor(3, dtype=torch.long),
                             "capture": torch.tensor(1, dtype=torch.long),
                             "promotion_piece": torch.tensor(0, dtype=torch.long)
                         })

    def test_move_to_targets_castle(self):
        # given
        move = CastleKingSide()

        # when
        result = transformer.move_to_targets(move)

        # then
        self.assertEqual(result,
                         {
                             "type": torch.tensor(1, dtype=torch.long),
                             "piece": torch.tensor(6, dtype=torch.long),
                             "source_file": torch.tensor(0, dtype=torch.long),
                             "source_rank": torch.tensor(0, dtype=torch.long),
                             "target_file": torch.tensor(0, dtype=torch.long),
                             "target_rank": torch.tensor(0, dtype=torch.long),
                             "capture": torch.tensor(0, dtype=torch.long),
                             "promotion_piece": torch.tensor(0, dtype=torch.long)
                         }
                         )
