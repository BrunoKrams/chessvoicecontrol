from test_data_generation.model.moves.board import File, Rank
from test_data_generation.model.moves.move import Move, Type
from test_data_generation.model.moves.pieces import Piece

def all():
    result = []
    for file in list(File):
        for piece in [p for p in list(Piece) if p.is_promotable]:
            result.append(PawnTakesWithPromotion(file, piece))
    return result

class PawnTakesWithPromotion(Move):
    def __init__(self, file:File, promoted_to:Piece):
        if not promoted_to.is_promotable:
            raise ValueError(f"{promoted_to} is not promotable")
        self.type = Type.PROMOTION
        self.piece = Piece.PAWN
        self.source_file = None
        self.source_rank = Rank.SEVENTH
        self.target_file = file
        self.target_rank = Rank.EIGHTTH
        self.capture = True
        self.promoted_to = promoted_to

    def san(self):
        return f"x{self.target_file}8={self.promoted_to.san}"

    def full_texts(self):
        result = []
        prefix = f"Bauer schlägt auf {self.target_file}8"
        suffixes = [f"Umwandlung {self._article(self.promoted_to)} {self.promoted_to.label}",
                    f"Umwandlung {self.promoted_to.label}",
                    f"{self.promoted_to.label}"]
        for suffix in suffixes:
            result.append(f"{prefix}, {suffix}")
        return result

    def _article(self, piece:Piece):
        match piece:
            case Piece.KNIGHT:
                return "zum"
            case Piece.BISHOP:
                return "zum"
            case Piece.ROOK:
                return "zum"
            case Piece.QUEEN:
                return "zur"

if __name__ == "__main__":
    for move in all():
        print(move.san())