from test_data_generation.model.moves.board import Square, get_file, get_rank
from test_data_generation.model.moves.move import Move, Type
from test_data_generation.model.moves.pieces import Piece

def all():
    result = []
    for takes in [True, False]:
        for piece in list(Piece):
            for square in list(Square):
                result.append(SimpleNonPawnMoveWithTargetOnly(piece, square, takes))
    return result

class SimpleNonPawnMoveWithTargetOnly(Move):
    def __init__(self, piece: Piece, target_square: Square, capture: bool = False):
        self.type = Type.STANDARD
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

    def full_texts(self):
        return [f"{self.piece.label} {"schlägt " if self.capture else ""}auf {self.target_square}",
                f"{self.piece.label} {"schlägt " if self.capture else ""}{self.target_square}",
                ]

if __name__ == "__main__":
    for move in all():
        print(move.san())