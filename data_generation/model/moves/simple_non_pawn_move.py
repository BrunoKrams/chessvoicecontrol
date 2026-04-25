from model.moves.board import Square
from model.moves.pieces import Piece

class SimpleNonPawnMove():
    def __init__(self, piece:Piece, source_square: Square, target_square: Square, takes:bool=False):
        self._piece = piece
        self.source_square = source_square
        self.target_square = target_square
        self.takes = takes

    def san(self):
        return f"{self._piece.san}{self.source_square}{"x" if self.takes else ""}{self.target_square}"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, SimpleNonPawnMove):
            return False
        return (self._piece == other._piece
                and self.source_square == other.source_square
                and self.target_square == other.target_square
                and self.takes == other.takes)

    def __hash__(self):
        return hash((self._piece, self.source_square, self.target_square, self.takes))

    def full_texts(self):
        return [f"{self._piece.label} {self.source_square} {"schlägt " if self.takes else ""}auf {self.target_square}",
                f"{self._piece.label} {self.source_square} {"schlägt " if self.takes else ""}{self.target_square}",
                ]

