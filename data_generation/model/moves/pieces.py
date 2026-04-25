import enum


class Piece(enum.Enum):
    PAWN = ("", "Bauer", False)
    KNIGHT = ("N", "Springer")
    BISHOP = ("B", "Läufer")
    ROOK = ("R", "Turm")
    QUEEN = ("Q", "Dame")
    KING = ("K", "König", False)

    def __init__(self, san: str, label: str, is_promotable:bool=True):
        self.san = san
        self.label = label
        self.is_promotable = is_promotable