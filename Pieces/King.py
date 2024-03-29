from Pieces.Piece import Piece


class King(Piece):

    alliance = None
    position = None

    def __init__(self, alliance, position):
        self.alliance = alliance
        self.position = position

    def to_string(self):
        return "K" if self.alliance == "Black" else "k"
