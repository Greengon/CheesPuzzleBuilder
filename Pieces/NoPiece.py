from Pieces.Piece import Piece


class NoPiece(Piece):
    def __init__(self):
        pass

    def to_string(self):
        return "-"
