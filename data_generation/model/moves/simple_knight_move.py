from model.moves.board import Square, get_rank,  get_file,  get_square
from model.moves.simple_non_pawn_move import SimpleNonPawnMove
from model.moves.pieces import Piece


def all():
    result = []
    for takes in [True, False]:
        for source_square in list(Square):
            for target_square in _get_reachable_squares(source_square):
                result.append(SimpleKnightMove(source_square, target_square, takes))
    return result

def _get_reachable_squares(source_square: Square):
    result = []
    offsets = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
    for file_offset, rank_offset in offsets:
        target_square = _move_(source_square, file_offset, rank_offset)
        if target_square != None:
            result.append(target_square)
    return result

def _move_(source_square, file_offset: int, rank_offset: int) -> Square | None:
    file = get_file(source_square) + file_offset
    rank = get_rank(source_square) + rank_offset
    if file is None or rank is None:
        return None
    return get_square(file, rank)

class SimpleKnightMove(SimpleNonPawnMove):
    def __init__(self, source_square: Square, target_square: Square, takes: bool = False):
        super().__init__(Piece.KNIGHT, source_square, target_square, takes)


if __name__ == '__main__':
    for move in all():
        print(move.san())
