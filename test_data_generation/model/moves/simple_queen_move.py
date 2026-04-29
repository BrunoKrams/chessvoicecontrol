from test_data_generation.model.moves.board import Square, get_diagonals, get_file, get_rank
from test_data_generation.model.moves.simple_non_pawn_move import SimpleNonPawnMove
from test_data_generation.model.moves.pieces import Piece

def all():
    result = []
    for takes in [True, False]:
        for source_square in list(Square):
            for target_square in (s for s in get_file(source_square).value if s != source_square):
                result.append(SimpleQueenMove(source_square, target_square,takes))
            for target_square in (s for s in get_rank(source_square).value if s != source_square):
                result.append(SimpleQueenMove(source_square, target_square, takes))
            for diagonal in get_diagonals(source_square):
                for target_square in (s for s in diagonal.value if s != source_square):
                    result.append(SimpleQueenMove(source_square, target_square, takes))
    return result

class SimpleQueenMove(SimpleNonPawnMove):
    def __init__(self, source_square: Square, target_square: Square, capture:bool = False):
        super().__init__(Piece.QUEEN, source_square, target_square, capture)

if __name__ == '__main__':
    for move in all():
        print(move.san())