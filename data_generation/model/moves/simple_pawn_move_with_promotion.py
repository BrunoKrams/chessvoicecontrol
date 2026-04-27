from model.moves.board import File, Rank
from model.moves.pieces import Piece

def all():
    result = []
    for piece in [p for p in list(Piece) if p.is_promotable]:
        for file in list(File):
            result.append(SimplePawnMoveWithPromotion(file, piece))
    return result

class SimplePawnMoveWithPromotion():
    def __init__(self, file:File, promoted_to:Piece):
        if not promoted_to.is_promotable:
            raise ValueError(f"{promoted_to} is not promotable")
        self.piece = Piece.PAWN
        self.source_file = file
        self.source_rank = Rank.SEVENTH
        self.target_file = file
        self.target_rank = Rank.EIGHTTH
        self.capture = False
        self.promoted_to = promoted_to

    def san(self):
        return f"{self.source_file}8={self.promoted_to.san}"

    def full_texts(self):
        result = []
        prefixes = [f"Bauer auf {self.source_file}8", f"{self.source_file}8"]
        suffixes = [f"Umwandlung {self._article(self.promoted_to)} {self.promoted_to.label}",
                    f"Umwandlung {self.promoted_to.label}",
                    f"{self.promoted_to.label}"]
        for prefix in prefixes:
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