from model.moves.board import Square, get_rank, get_file, get_square, File
from model.moves.simple_non_pawn_move_with_file_and_target import SimpleNonPawnMoveWithFileAndTarget
from model.moves.pieces import Piece

def all():
    result = []
    for takes in [True, False]:
        for file in list(File):
            for source_square in file.value:
                for target_square in _get_reachable_squares(source_square):
                    result.append(SimpleKnightMoveWithFileAndTarget(file, target_square, takes))
    result = list(set(result)) # removes duplicates
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

class SimpleKnightMoveWithFileAndTarget(SimpleNonPawnMoveWithFileAndTarget):
    def __init__(self, file: File, target_square: Square, capture: bool = False):
        super().__init__(Piece.KNIGHT, file, target_square, capture)


if __name__ == '__main__':
    for move in all():
        print(move.san())
