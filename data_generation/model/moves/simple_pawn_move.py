from model.moves.board import Square, Rank, get_file, get_rank
from model.moves.pieces import Piece


def all():
    return [SimplePawnMove(square) for square in list(Square) if square not in [*Rank.FIRST.value, *Rank.SECOND.value, *Rank.EIGHTTH.value]]

class SimplePawnMove():
    def __init__(self, target_square: Square):
        self.piece = Piece.PAWN
        self.source_file = get_file(target_square)
        self.source_rank = None
        self.target_file = get_file(target_square)
        self.target_rank = get_rank(target_square)
        self.capture = False
        self.promoted_to = None

        self._target_square = target_square

    def san(self):
        return str(self._target_square)

    def full_texts(self):
        return [f"Bauer auf {self._target_square}",
                f"Bauer {self._target_square}",
                f"{self._target_square}"
                ]
