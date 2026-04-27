import enum
import functools
from typing import List

class Square(enum.Enum):
    A1 =  1;  A2 =  2;  A3 =  3;  A4 =  4;  A5 =  5;  A6 =  6;  A7 =  7;  A8 =  8
    B1 =  9;  B2 = 10;  B3 = 11;  B4 = 12;  B5 = 13;  B6 = 14;  B7 = 15;  B8 = 16
    C1 = 17;  C2 = 18;  C3 = 19;  C4 = 20;  C5 = 21;  C6 = 22;  C7 = 23;  C8 = 24
    D1 = 25;  D2 = 26;  D3 = 27;  D4 = 28;  D5 = 29;  D6 = 30;  D7 = 31;  D8 = 32
    E1 = 33;  E2 = 34;  E3 = 35;  E4 = 36;  E5 = 37;  E6 = 38;  E7 = 39;  E8 = 40
    F1 = 41;  F2 = 42;  F3 = 43;  F4 = 44;  F5 = 45;  F6 = 46;  F7 = 47;  F8 = 48
    G1 = 49;  G2 = 50;  G3 = 51;  G4 = 52;  G5 = 53;  G6 = 54;  G7 = 55;  G8 = 56
    H1 = 57;  H2 = 58;  H3 = 59;  H4 = 60;  H5 = 61;  H6 = 62;  H7 = 63;  H8 = 64

    def __str__(self):
        return self.name.lower()


class Diagonal(enum.Enum):
    A1_H8 = (Square.A1, Square.B2, Square.C3, Square.D4, Square.E5, Square.F6, Square.G7, Square.H8)
    A2_G8 = (Square.A2, Square.B3, Square.C4, Square.D5, Square.E6, Square.F7, Square.G8)
    A3_F8 = (Square.A3, Square.B4, Square.C5, Square.D6, Square.E7, Square.F8)
    A4_E8 = (Square.A4, Square.B5, Square.C6, Square.D7, Square.E8)
    A5_D8 = (Square.A5, Square.B6, Square.C7, Square.D8)
    A6_C8 = (Square.A6, Square.B7, Square.C8)
    A7_B8 = (Square.A7, Square.B8)

    B1_H7 = (Square.B1, Square.C2, Square.D3, Square.E4, Square.F5, Square.G6, Square.H7)
    C1_H6 = (Square.C1, Square.D2, Square.E3, Square.F4, Square.G5, Square.H6)
    D1_H5 = (Square.D1, Square.E2, Square.F3, Square.G4, Square.H5)
    E1_H4 = (Square.E1, Square.F2, Square.G3, Square.H4)
    F1_H3 = (Square.F1, Square.G2, Square.H3)
    G1_H2 = (Square.G1, Square.H2)

    H1_A8 = (Square.H1, Square.G2, Square.F3, Square.E4, Square.D5, Square.C6, Square.B7, Square.A8)
    H2_B8 = (Square.H2, Square.G3, Square.F4, Square.E5, Square.D6, Square.C7, Square.B8)
    H3_C8 = (Square.H3, Square.G4, Square.F5, Square.E6, Square.D7, Square.C8)
    H4_D8 = (Square.H4, Square.G5, Square.F6, Square.E7, Square.D8)
    H5_E8 = (Square.H5, Square.G6, Square.F7, Square.E8)
    H6_F8 = (Square.H6, Square.G7, Square.F8)
    H7_G8 = (Square.H7, Square.G8)

    B1_A2 = (Square.B1, Square.A2)
    C1_A3 = (Square.C1, Square.B2, Square.A3)
    D1_A4 = (Square.D1, Square.C2, Square.B3, Square.A4)
    E1_A5 = (Square.E1, Square.D2, Square.C3, Square.B4, Square.A5)
    F1_A6 = (Square.F1, Square.E2, Square.D3, Square.C4, Square.B5, Square.A6)
    G1_A7 = (Square.G1, Square.F2, Square.E3, Square.D4, Square.C5, Square.B6, Square.A7)

@functools.total_ordering
class Rank(enum.Enum):
    FIRST   = (Square.A1, Square.B1, Square.C1, Square.D1, Square.E1, Square.F1, Square.G1, Square.H1)
    SECOND  = (Square.A2, Square.B2, Square.C2, Square.D2, Square.E2, Square.F2, Square.G2, Square.H2)
    THIRD   = (Square.A3, Square.B3, Square.C3, Square.D3, Square.E3, Square.F3, Square.G3, Square.H3)
    FOURTH  = (Square.A4, Square.B4, Square.C4, Square.D4, Square.E4, Square.F4, Square.G4, Square.H4)
    FIFTH   = (Square.A5, Square.B5, Square.C5, Square.D5, Square.E5, Square.F5, Square.G5, Square.H5)
    SIXTH   = (Square.A6, Square.B6, Square.C6, Square.D6, Square.E6, Square.F6, Square.G6, Square.H6)
    SEVENTH = (Square.A7, Square.B7, Square.C7, Square.D7, Square.E7, Square.F7, Square.G7, Square.H7)
    EIGHTTH = (Square.A8, Square.B8, Square.C8, Square.D8, Square.E8, Square.F8, Square.G8, Square.H8)

    def __lt__(self, other: "Rank") -> bool:
        members = list(Rank)
        return members.index(self) < members.index(other)

    def __eq__(self, other: object) -> bool:
        return self is other

    def __hash__(self):
        return hash(self.name)

    def __add__(self, steps: int) -> "Rank | None":
        members = list(Rank)
        new_index = members.index(self) + steps
        return members[new_index] if 0 <= new_index < len(members) else None

    def __sub__(self, steps: int) -> "Rank | None":
        return self.__add__(-steps)

@functools.total_ordering
class File(enum.Enum):
    A = (Square.A1, Square.A2, Square.A3, Square.A4, Square.A5, Square.A6, Square.A7, Square.A8)
    B = (Square.B1, Square.B2, Square.B3, Square.B4, Square.B5, Square.B6, Square.B7, Square.B8)
    C = (Square.C1, Square.C2, Square.C3, Square.C4, Square.C5, Square.C6, Square.C7, Square.C8)
    D = (Square.D1, Square.D2, Square.D3, Square.D4, Square.D5, Square.D6, Square.D7, Square.D8)
    E = (Square.E1, Square.E2, Square.E3, Square.E4, Square.E5, Square.E6, Square.E7, Square.E8)
    F = (Square.F1, Square.F2, Square.F3, Square.F4, Square.F5, Square.F6, Square.F7, Square.F8)
    G = (Square.G1, Square.G2, Square.G3, Square.G4, Square.G5, Square.G6, Square.G7, Square.G8)
    H = (Square.H1, Square.H2, Square.H3, Square.H4, Square.H5, Square.H6, Square.H7, Square.H8)

    def __str__(self):
        return self.name.lower()

    def __lt__(self, other: "File") -> bool:
        members = list(File)
        return members.index(self) < members.index(other)

    def __eq__(self, other: object) -> bool:
        return self is other

    def __hash__(self):
        return hash(self.name)

    def __add__(self, steps: int) -> "File | None":
        members = list(File)
        new_index = members.index(self) + steps
        return members[new_index] if 0 <= new_index < len(members) else None

    def __sub__(self, steps: int) -> "File | None":
        return self.__add__(-steps)

def get_diagonals(square: Square) -> List[Diagonal]:
    result = []
    for diagonal in list(Diagonal):
        if square in diagonal.value:
            result.append(diagonal)
    return result

def get_file(square: Square) -> File:
    for file in list(File):
        if square in file.value:
            return file

def get_rank(square: Square) -> Rank:
    for rank in list(Rank):
        if square in rank.value:
            return rank

def get_square(file: File, rank: Rank) -> Square:
    rank_index = list(Rank).index(rank)
    return file.value[rank_index]

def get_square(file:File, rank:Rank) -> Square:
    for square in list(Square):
        if square in file.value and square in rank.value:
            return square