from model.moves.board import Square, get_rank, get_file
from model.moves.pieces import Piece

class SimpleNonPawnMove():
    def __init__(self, piece:Piece, source_square: Square, target_square: Square, capture:bool=False):
        self.piece = piece
        self.source_file = get_file(source_square)
        self.source_rank = get_rank(source_square)
        self.target_file = get_file(target_square)
        self.target_rank = get_rank(target_square)
        self.capture = capture
        self.promoted_to = None

        self.source_square = source_square
        self.target_square = target_square

    def san(self):
        return f"{self.piece.san}{self.source_square}{"x" if self.capture else ""}{self.target_square}"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, SimpleNonPawnMove):
            return False
        return (self.piece == other.piece
                and self.source_square == other.source_square
                and self.target_square == other.target_square
                and self.capture == other.capture)

    def __hash__(self):
        return hash((self.piece, self.source_square, self.target_square, self.capture))

    def full_texts(self):
        return [f"{self.piece.label} {self.source_square} {"schlägt " if self.capture else ""}auf {self.target_square}",
                f"{self.piece.label} {self.source_square} {"schlägt " if self.capture else ""}{self.target_square}",
                ]

