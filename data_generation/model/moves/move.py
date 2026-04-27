import enum
from abc import ABC
from dataclasses import dataclass
from typing import Any

from model.moves.board import File, Rank
from model.moves.pieces import Piece

class Type(enum.Enum):
    STANDARD = 0
    CASTLE_KING_SIDE = 1
    CASTLE_QUEEN_SIDE = 2
    PROMOTION = 3

@dataclass
class Move(ABC):
    type: Type
    piece: Piece
    source_file: File | None
    source_rank: Rank | None
    target_file: File | None
    target_rank: Rank | None
    capture: bool = False
    promoted_to: Piece | None = None

## TODO add masks for the different types

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Move):
            return NotImplemented
        return (
            self.type == other.type
            and self.piece == other.piece
            and self.source_file == other.source_file
            and self.source_rank == other.source_rank
            and self.target_file == other.target_file
            and self.target_rank == other.target_rank
            and self.capture == other.capture
            and self.promoted_to == other.promoted_to
        )

    def __hash__(self) -> int:
        return hash(
            (
                self.type,
                self.piece,
                self.source_file,
                self.source_rank,
                self.target_file,
                self.target_rank,
                self.capture,
                self.promoted_to,
            )
        )

