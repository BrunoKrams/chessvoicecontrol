from model.moves.board import Square, File, get_diagonals
from model.moves.simple_non_pawn_move_with_file_and_target import SimpleNonPawnMoveWithFileAndTarget
from model.moves.pieces import Piece

def all():
    result = []
    for takes in [True, False]:
        for file in list(File):
            for source_square in file.value:
                for diagonal in get_diagonals(source_square):
                    for target_square in (s for s in diagonal.value if s != source_square):
                        result.append(SimpleBishopMoveWithFileAndTarget(file, target_square, takes))
    result = list(set(result))
    return result

class SimpleBishopMoveWithFileAndTarget(SimpleNonPawnMoveWithFileAndTarget):
    def __init__(self, file: File, target_square: Square, takes: bool = False):
        super().__init__(Piece.BISHOP, file, target_square, takes)


if __name__ == '__main__':
    for move in all():
        print(move.san())
