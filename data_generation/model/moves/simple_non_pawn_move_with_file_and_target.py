from argparse import ArgumentError

from model.moves.board import Square, File
from model.moves.pieces import Piece

class SimpleNonPawnMoveWithFileAndTarget():
    def __init__(self, piece: Piece, file:File, target_square: Square, takes: bool = False):
        if piece not in [Piece.KNIGHT, Piece.BISHOP, Piece.ROOK]:
            raise ArgumentError
        self._piece = piece
        self.file = file
        self.target_square = target_square
        self.takes = takes

    def san(self):
        return f"{self._piece.san}{self.file}{"x" if self.takes else ""}{self.target_square}"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, SimpleNonPawnMoveWithFileAndTarget):
            return False
        return (self._piece == other._piece
                and self.file == other.file
                and self.target_square == other.target_square
                and self.takes == other.takes)

    def __hash__(self):
        return hash((self._piece, self.file, self.target_square, self.takes))

    def full_texts(self):
        return [f"{self._piece.label} {self.file} {"schlägt " if self.takes else ""}auf {self.target_square}",
                f"{self._piece.label} {self.file} {"schlägt " if self.takes else ""}{self.target_square}",
                f"{self._piece.label} auf der {self.file}-Linie {"schlägt " if self.takes else ""}auf {self.target_square}",
                f"{self._piece.label} auf der {self.file}-Linie {"schlägt " if self.takes else ""}{self.target_square}",
                f"Der {self.file}-{self._piece.label} {"schlägt " if self.takes else ""}auf {self.target_square}",
                f"Der {self.file}-{self._piece.label} {"schlägt " if self.takes else ""}{self.target_square}",
                f"Der {self._piece.label} auf der {self.file}-Linie {"schlägt " if self.takes else ""}auf {self.target_square}",
                f"Der {self._piece.label} auf der {self.file}-Linie {"schlägt " if self.takes else ""}{self.target_square}",
                ]

if __name__ == "__main__":
    for move in all():
        print(move.san())