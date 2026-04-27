from model.moves.board import Square, File, Rank, get_square, get_file, get_rank
from model.moves.pieces import Piece


def all():
    result = []
    for file in list(File):
        for rank in list(Rank):
            if rank >= Rank.THIRD and rank < Rank.EIGHTTH:
                left_file = file -1
                if left_file is not None:
                    result.append(PawnTakesMoveWithFile(file, get_square(left_file, rank)))
                right_file = file +1
                if right_file is not None:
                    result.append(PawnTakesMoveWithFile(file, get_square(right_file, rank)))
    return result


class PawnTakesMoveWithFile():
    def __init__(self, file: File, target_square: Square):
        self.piece = Piece.PAWN
        self.source_file = file
        self.source_rank = None
        self.target_file = get_file(target_square)
        self.target_rank = get_rank(target_square)
        self.capture = False
        self.promoted_to = None
        self._target_square = target_square

    def san(self):
        return f"{self.source_file}x{self._target_square}"

    def full_texts(self):
        return [f"{self.source_file}-Bauer schlägt auf {self._target_square}",
                f"{self.source_file}-Bauer schlägt {self._target_square}",
                f"Der {self.source_file}-Bauer schlägt auf {self._target_square}",
                f"Der {self.source_file}-Bauer schlägt {self._target_square}",
                f"{self.source_file} schlägt {self._target_square}",
                f"{self.source_file} schlägt auf {self._target_square}",
                ]

if __name__ == "__main__":
    for move in all():
        print(move.san())