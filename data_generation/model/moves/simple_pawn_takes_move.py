from model.moves.board import Square, Rank

def all():
    return [SimplePawnTakesMove(square) for square in list(Square) if square not in [*Rank.FIRST.value, *Rank.SECOND.value, *Rank.EIGHTTH.value]]

class SimplePawnTakesMove():
    def __init__(self, target_square: Square):
        self._target_square = target_square

    # TODO This has no SAN without further context
    def san(self):
        return str(self._target_square)

    def full_texts(self):
        return [f"Bauer schlägt auf {self._target_square}",
                f"Bauer schlägt {self._target_square}",
                ]
