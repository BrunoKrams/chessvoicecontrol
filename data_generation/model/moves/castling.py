from data_generation.model.moves.move import move
from data_generation.model.pieces import Piece


def all():
    return [CastleQueenSide(), CastleQueenSide()]

class CastleKingSide(move):
    def id(self):
        return "castle_kingside"

    def san(self):
        return "0-0"

    def full_texts(self) -> list[str]:
        return ["Kurze Rochade", "Rochade am Königsflügel", "Rochade Königsflügel"]

class CastleQueenSide():
    def san(self):
        return "0-0-0"

    def full_texts(self) -> list[str]:
        return ["Lange Rochade", "Rochade am Damenflügel", "Rochade Damenflügel"]

