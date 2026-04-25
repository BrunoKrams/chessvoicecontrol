def all():
    return [CastleQueenSide(), CastleQueenSide()]

class CastleKingSide():
    def san(self):
        return "0-0"

    def full_texts(self) -> list[str]:
        return ["Kurze Rochade", "Rochade am Königsflügel", "Rochade Königsflügel"]

class CastleQueenSide():
    def san(self):
        return "0-0-0"

    def full_texts(self) -> list[str]:
        return ["Lange Rochade", "Rochade am Damenflügel", "Rochade Damenflügel"]

