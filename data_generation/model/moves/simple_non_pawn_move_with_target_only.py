from model.moves.board import Square, get_file, get_rank
from model.moves.pieces import Piece

def all():
    result = []
    for takes in [True, False]:
        for piece in list(Piece):
            for square in list(Square):
                result.append(SimpleNonPawnMoveWithTargetOnly(piece, square, takes))
    return result

class SimpleNonPawnMoveWithTargetOnly():
    def __init__(self, piece: Piece, target_square: Square, capture: bool = False):
        self.piece = piece
        self.source_file = None
        self.source_rank = None
        self.target_file = get_file(target_square)
        self.target_rank = get_rank(target_square)
        self.capture = capture
        self.promoted_to = None

        self.target_square = target_square

    def san(self):
        return f"{self.piece.san}{"x" if self.capture else ""}{self.target_square}"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, SimpleNonPawnMoveWithTargetOnly):
            return False
        return (self.piece == other.piece
                and self.target_square == other.target_square
                and self.capture == other.capture)

    def __hash__(self):
        return hash((self.piece, self.target_square, self.capture))

    def full_texts(self):
        return [f"{self.piece.label} {"schlägt " if self.capture else ""}auf {self.target_square}",
                f"{self.piece.label} {"schlägt " if self.capture else ""}{self.target_square}",
                ]

if __name__ == "__main__":
    for move in all():
        print(move.san())