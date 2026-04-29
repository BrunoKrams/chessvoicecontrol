from typing import Dict, TypedDict

import torch

from model.moves.board import File, Rank
from model.moves.move import Type
from model.moves.pieces import Piece

type_mapping = {
    Type.STANDARD: 0,
    Type.CASTLE_KING_SIDE: 1,
    Type.CASTLE_QUEEN_SIDE: 2,
    Type.PROMOTION: 3
}

piece_mapping = {
    None: 0,
    Piece.PAWN: 1,
    Piece.KNIGHT: 2,
    Piece.BISHOP: 3,
    Piece.ROOK: 4,
    Piece.QUEEN: 5,
    Piece.KING: 6,
}

file_mapping = {
    None: 0,
    File.A: 1,
    File.B: 2,
    File.C: 3,
    File.D: 4,
    File.E: 5,
    File.F: 6,
    File.G: 7,
    File.H: 8,
}

rank_mapping = {
    None: 0,
    Rank.FIRST: 1,
    Rank.SECOND: 2,
    Rank.THIRD: 3,
    Rank.FOURTH: 4,
    Rank.FIFTH: 5,
    Rank.SIXTH: 6,
    Rank.SEVENTH: 7,
    Rank.EIGHTTH: 8,
}

def _create_long_tensor(value: int):
    return torch.tensor(value, dtype=torch.long)


def move_to_targets(move) -> Dict[str, torch.Tensor]:
    return {
        "type": _create_long_tensor(type_mapping[move.type]),
        "piece": _create_long_tensor(piece_mapping[move.piece]),
        "source_file": _create_long_tensor(file_mapping[move.source_file]),
        "source_rank": _create_long_tensor(rank_mapping[move.source_rank]),
        "target_file": _create_long_tensor(file_mapping[move.target_file]),
        "target_rank": _create_long_tensor(rank_mapping[move.target_rank]),
        "capture": _create_long_tensor(1 if move.capture else 0),
        "promotion_piece": _create_long_tensor(piece_mapping[move.promoted_to]),
    }
