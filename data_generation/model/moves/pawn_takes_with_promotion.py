from chess import Move

from model.moves.board import File
from model.moves.pieces import Piece

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
        self._file = file
        self._promoted_to = promoted_to

    def san(self):
        return f"x{self._file}8={self._promoted_to.san}"

    def full_texts(self):
        result = []
        prefix = f"Bauer schlägt auf {self._file}8"
        suffixes = [f"Umwandlung {self._article(self._promoted_to)} {self._promoted_to.label}",
                    f"Umwandlung {self._promoted_to.label}",
                    f"{self._promoted_to.label}"]
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