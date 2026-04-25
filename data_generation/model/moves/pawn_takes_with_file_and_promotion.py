from chess import Move

from model.moves.board import File
from model.moves.pieces import Piece

def all():
    result = []
    for piece in [p for p in list(Piece) if p.is_promotable]:
        result.append(PawnTakesWithFileAndPromotion(File.A, File.B, piece))
        result.append(PawnTakesWithFileAndPromotion(File.H, File.G, piece))
        for file in [File.B, File.C, File.D, File.E, File.F, File.G]:
            result.append(PawnTakesWithFileAndPromotion(file, file - 1, piece))
            result.append(PawnTakesWithFileAndPromotion(file, file + 1, piece))
    return result

class PawnTakesWithFileAndPromotion(Move):
    def __init__(self, source_file:File, target_file:File, promoted_to:Piece):
        if not promoted_to.is_promotable:
            raise ValueError(f"{promoted_to} is not promotable")
        self._source_file = source_file
        self._target_file = target_file
        self._promoted_to = promoted_to

    def san(self):
        return f"{self._source_file}7x{self._target_file}8={self._promoted_to.san}"

    def full_texts(self):
        result = []
        prefixes = [f"Bauer {self._source_file} schlägt auf {self._target_file}8",
                    f"{self._source_file} schlägt auf {self._target_file}8",
                    f"Der {self._source_file}-Bauer schlägt auf {self._target_file}8",
                    f"{self._source_file}-Bauer schlägt auf {self._target_file}8",
                    f"{self._source_file} schlägt auf {self._target_file}8",
                    f"Bauer {self._source_file} schlägt {self._target_file}8",
                    f"{self._source_file} schlägt {self._target_file}8",
                    f"Der {self._source_file}-Bauer schlägt {self._target_file}8",
                    f"{self._source_file}-Bauer schlägt {self._target_file}8",
                    f"{self._source_file} schlägt {self._target_file}8",
                    ]
        suffixes = [f"Umwandlung {self._article(self._promoted_to)} {self._promoted_to.label}",
                    f"Umwandlung {self._promoted_to.label}",
                    f"{self._promoted_to.label}"]
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