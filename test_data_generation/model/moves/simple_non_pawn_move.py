from test_data_generation.model.moves.board import Square, get_rank, get_file
from test_data_generation.model.moves.move import Move, Type
from test_data_generation.model.moves.pieces import Piece

class SimpleNonPawnMove(Move):
    def __init__(self, piece:Piece, source_square: Square, target_square: Square, capture:bool=False):
        self.type = Type.STANDARD
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

    def full_texts(self):
        return [f"{self.piece.label} {self.source_square} {"schlägt " if self.capture else ""}auf {self.target_square}",
                f"{self.piece.label} {self.source_square} {"schlägt " if self.capture else ""}{self.target_square}",
                ]

