import enum
from abc import ABC
from dataclasses import dataclass, fields
from typing import Any, Dict

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
    capture: bool | None = False
    promoted_to: Piece | None = None

    def identifier(self):
        return "_".join([
            self.type.name,
            self.piece.name,
            self.source_file.name if self.source_file else "X",
            self.source_rank.name if self.source_rank else "X",
            self.target_file.name if self.target_file else "X",
            self.target_rank.name if self.target_rank else "X",
            "1" if self.capture else "0",
            self.promoted_to.name if self.promoted_to else "X",
        ])


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
