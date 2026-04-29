from dataclasses import dataclass
from typing import Dict

from test_data_generation.model.moves.move import Type


@dataclass
class Mask:
    piece_mask: int
    source_file_mask: int
    source_rank_mask: int
    target_file_mask: int
    target_rank_mask: int
    capture_mask: int
    promotion_piece_mask: int


type_masks: Dict[Type, Mask] = {
    Type.STANDARD: Mask(
        piece_mask=1,
        source_file_mask=1,
        source_rank_mask=1,
        target_file_mask=1,
        target_rank_mask=1,
        capture_mask=1,
        promotion_piece_mask=0,
    ),
    Type.CASTLE_KING_SIDE: Mask(
        piece_mask=1,
        source_file_mask=0,
        source_rank_mask=0,
        target_file_mask=0,
        target_rank_mask=0,
        capture_mask=0,
        promotion_piece_mask=0,
    ),
    Type.CASTLE_QUEEN_SIDE: Mask(
        piece_mask=1,
        source_file_mask=0,
        source_rank_mask=0,
        target_file_mask=0,
        target_rank_mask=0,
        capture_mask=0,
        promotion_piece_mask=0,
    ),
    Type.PROMOTION: Mask(
        piece_mask=1,
        source_file_mask=1,
        source_rank_mask=1,
        target_file_mask=1,
        target_rank_mask=1,
        capture_mask=1,
        promotion_piece_mask=1,
    ),
}