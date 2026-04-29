from test_data_generation.model.moves.board import Square, Rank, get_rank, get_file
from test_data_generation.model.moves.move import Move, Type
from test_data_generation.model.moves.pieces import Piece


def all():
    return [SimplePawnTakesMove(square) for square in list(Square) if square not in [*Rank.FIRST.value, *Rank.SECOND.value, *Rank.EIGHTTH.value]]

class SimplePawnTakesMove(Move):
    def __init__(self, target_square: Square):
        self.type = Type.STANDARD
        self.piece = Piece.PAWN
        self.source_file= None
        self.source_rank = None
        self.target_file = get_file(target_square)
        self.target_rank = get_rank(target_square)
        self.capture = True
        self.promoted_to = None
        self._target_square = target_square

    def san(self):
        return str(self._target_square)

    def full_texts(self):
        return [f"Bauer schlägt auf {self._target_square}",
                f"Bauer schlägt {self._target_square}",
                ]
