from model.moves.move import Move, Type
from model.moves.pieces import Piece


def all():
    return [CastleQueenSide(), CastleQueenSide()]

class CastleKingSide(Move):
    def __init__(self):
        self.type = Type.CASTLE_KING_SIDE
        self.piece = Piece.KING
        self.source_file = None
        self.source_rank = None
        self.target_file = None
        self.target_rank = None
        self.capture = False
        self.promoted_to = None

    def id(self):
        return "castle_kingside"

    def san(self):
        return "0-0"

    def full_texts(self) -> list[str]:
        return ["Kurze Rochade", "Rochade am Königsflügel", "Rochade Königsflügel"]

class CastleQueenSide():
    def __init__(self):
        self.type = Type.CASTLE_QUEEN_SIDE
        self.piece = Piece.KING
        self.source_file = None
        self.source_rank = None
        self.target_file = None
        self.target_rank = None
        self.capture = False
        self.promoted_to = None

    def san(self):
        return "0-0-0"

    def full_texts(self) -> list[str]:
        return ["Lange Rochade", "Rochade am Damenflügel", "Rochade Damenflügel"]

