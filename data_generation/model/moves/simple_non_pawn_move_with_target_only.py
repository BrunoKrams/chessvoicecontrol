from model.moves.board import Square
from model.moves.pieces import Piece

def all():
    result = []
    for takes in [True, False]:
        for piece in list(Piece):
            for square in list(Square):
                result.append(SimpleNonPawnMoveWithTargetOnly(piece, square, takes))
    return result

class SimpleNonPawnMoveWithTargetOnly():
    def __init__(self, piece: Piece, target_square: Square, takes: bool = False):
        self._piece = piece
        self.target_square = target_square
        self.takes = takes

    def san(self):
        return f"{self._piece.san}{"x" if self.takes else ""}{self.target_square}"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, SimpleNonPawnMoveWithTargetOnly):
            return False
        return (self._piece == other._piece
                and self.target_square == other.target_square
                and self.takes == other.takes)

    def __hash__(self):
        return hash((self._piece, self.target_square, self.takes))

    def full_texts(self):
        return [f"{self._piece.label} {"schlägt " if self.takes else ""}auf {self.target_square}",
                f"{self._piece.label} {"schlägt " if self.takes else ""}{self.target_square}",
                ]

if __name__ == "__main__":
    for move in all():
        print(move.san())