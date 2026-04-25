from model.moves import (
    castling,
    pawn_takes_with_file_and_promotion,
    pawn_takes_with_file,
    pawn_takes_with_promotion,
    simple_bishop_move,
    simple_bishop_move_with_file_and_target,
    simple_king_move,
    simple_knight_move,
    simple_knight_move_with_file_and_target,
    simple_non_pawn_move_with_target_only,
    simple_pawn_move,
    simple_pawn_move_with_promotion,
    simple_pawn_takes_move,
    simple_queen_move,
    simple_rook_move,
    simple_rook_move_with_file_and_target,
)


def all():
    return [
        *castling.all(),
        *pawn_takes_with_file_and_promotion.all(),
        *pawn_takes_with_file.all(),
        *pawn_takes_with_promotion.all(),
        *simple_bishop_move.all(),
        *simple_bishop_move_with_file_and_target.all(),
        *simple_king_move.all(),
        *simple_knight_move.all(),
        *simple_knight_move_with_file_and_target.all(),
        *simple_non_pawn_move_with_target_only.all(),
        *simple_pawn_move.all(),
        *simple_pawn_move_with_promotion.all(),
        *simple_pawn_takes_move.all(),
        *simple_queen_move.all(),
        *simple_rook_move.all(),
        *simple_rook_move_with_file_and_target.all(),
    ]

if __name__ == "__main__":
    print(len(all()))
