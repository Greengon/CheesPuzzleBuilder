from Pieces.Piece import Piece


class NoPiece(Piece):
    position = None

    def __init__(self, given_position):
        self.position = given_position

    def to_string(self):
        return "-"
