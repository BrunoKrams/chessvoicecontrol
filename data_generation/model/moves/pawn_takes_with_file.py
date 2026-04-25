from model.moves.board import Square, File, Rank, get_square


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
        self._file = file
        self._target_square = target_square

    def san(self):
        return f"{self._file}x{self._target_square}"

    def full_texts(self):
        return [f"{self._file}-Bauer schlägt auf {self._target_square}",
                f"{self._file}-Bauer schlägt {self._target_square}",
                f"Der {self._file}-Bauer schlägt auf {self._target_square}",
                f"Der {self._file}-Bauer schlägt {self._target_square}",
                f"{self._file} schlägt {self._target_square}",
                f"{self._file} schlägt auf {self._target_square}",
                ]

if __name__ == "__main__":
    for move in all():
        print(move.san())