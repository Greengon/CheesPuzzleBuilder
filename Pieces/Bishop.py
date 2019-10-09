from Pieces.Piece import Piece


class Bishop(Piece):

    alliance = None
    position = None

    def __init__(self, alliance, position):
        self.alliance = alliance
        self.position = position

    def to_string(self):
        return "B" if self.alliance == "Black" else "b"
