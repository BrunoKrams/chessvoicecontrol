from model.moves.board import Square, get_rank, get_file
from model.moves.simple_non_pawn_move import SimpleNonPawnMove
from model.moves.pieces import Piece


def all():
    result = []
    for takes in [True, False]:
        for source_square in list(Square):
            for target_square in (s for s in get_file(source_square).value if s != source_square):
                result.append(SimpleRookMove(source_square, target_square, takes))
            for target_square in (s for s in get_rank(source_square).value if s != source_square):
                result.append(SimpleRookMove(source_square, target_square, takes))
    return result


class SimpleRookMove(SimpleNonPawnMove):
    def __init__(self, source_square: Square, target_square: Square, capture:bool = False):
        super().__init__(Piece.ROOK, source_square, target_square, capture)


if __name__ == '__main__':
    for move in all():
        print(move.san())
