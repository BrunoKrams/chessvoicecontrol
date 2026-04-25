from model.moves.board import Square, File
from model.moves.simple_non_pawn_move_with_file_and_target import SimpleNonPawnMoveWithFileAndTarget
from model.moves.pieces import Piece

def all():
    result = []
    for takes in [True, False]:
        for file in list(File):
            for square in list(Square):
                result.append(SimpleRookMoveWithFileAndTarget(file, square, takes))
    return result

class SimpleRookMoveWithFileAndTarget(SimpleNonPawnMoveWithFileAndTarget):
    def __init__(self, file: File, target_square: Square, takes: bool = False):
        super().__init__(Piece.ROOK, file, target_square, takes)


if __name__ == '__main__':
    for move in all():
        print(move.san())
