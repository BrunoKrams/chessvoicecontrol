from argparse import ArgumentError

from model.moves.board import Square, File, get_rank, get_file
from model.moves.pieces import Piece

class SimpleNonPawnMoveWithFileAndTarget():
    def __init__(self, piece: Piece, file:File, target_square: Square, capture: bool = False):
        if piece not in [Piece.KNIGHT, Piece.BISHOP, Piece.ROOK]:
            raise ArgumentError
        self.piece = piece
        self.source_file = file
        self.source_rank = None
        self.target_file = get_file(target_square)
        self.target_rank = get_rank(target_square)
        self.capture = capture
        self.promoted_to = None

        self.target_square = target_square

    def san(self):
        return f"{self.piece.san}{self.source_file}{"x" if self.capture else ""}{self.target_square}"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, SimpleNonPawnMoveWithFileAndTarget):
            return False
        return (self.piece == other.piece
                and self.source_file == other.source_file
                and self.target_square == other.target_square
                and self.capture == other.capture)

    def __hash__(self):
        return hash((self.piece, self.source_file, self.target_square, self.capture))

    def full_texts(self):
        return [f"{self.piece.label} {self.source_file} {"schlägt " if self.capture else ""}auf {self.target_square}",
                f"{self.piece.label} {self.source_file} {"schlägt " if self.capture else ""}{self.target_square}",
                f"{self.piece.label} auf der {self.source_file}-Linie {"schlägt " if self.capture else ""}auf {self.target_square}",
                f"{self.piece.label} auf der {self.source_file}-Linie {"schlägt " if self.capture else ""}{self.target_square}",
                f"Der {self.source_file}-{self.piece.label} {"schlägt " if self.capture else ""}auf {self.target_square}",
                f"Der {self.source_file}-{self.piece.label} {"schlägt " if self.capture else ""}{self.target_square}",
                f"Der {self.piece.label} auf der {self.source_file}-Linie {"schlägt " if self.capture else ""}auf {self.target_square}",
                f"Der {self.piece.label} auf der {self.source_file}-Linie {"schlägt " if self.capture else ""}{self.target_square}",
                ]

if __name__ == "__main__":
    for move in all():
        print(move.san())