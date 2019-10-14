from Board.Tile import Tile
from Pieces.NoPiece import NoPiece
from Pieces.Bishop import Bishop
from Pieces.King import King
from Pieces.Knight import Knight
from Pieces.Pawn import Pawn
from Pieces.Queen import Queen
from Pieces.Rook import Rook


class ChessBoard:

    gameTiles = {}

    def __init__(self):
        pass

    def create_board(self):
        self.gameTiles[0] = Tile(Rook("Black", 0), 0)
        self.gameTiles[1] = Tile(Knight("Black", 1), 1)
        self.gameTiles[2] = Tile(Bishop("Black", 2), 2)
        self.gameTiles[3] = Tile(Queen("Black", 3), 3)
        self.gameTiles[4] = Tile(King("Black", 4), 4)
        self.gameTiles[5] = Tile(Bishop("Black", 5), 5)
        self.gameTiles[6] = Tile(Knight("Black", 6), 6)
        self.gameTiles[7] = Tile(Rook("Black", 7), 7)
        self.gameTiles[8] = Tile(Pawn("Black", 8), 8)
        self.gameTiles[9] = Tile(Pawn("Black", 9), 9)
        self.gameTiles[10] = Tile(Pawn("Black", 10), 10)
        self.gameTiles[11] = Tile(Pawn("Black", 11), 11)
        self.gameTiles[12] = Tile(Pawn("Black", 12), 12)
        self.gameTiles[13] = Tile(Pawn("Black", 13), 13)
        self.gameTiles[14] = Tile(Pawn("Black", 14), 14)
        self.gameTiles[15] = Tile(Pawn("Black", 15), 15)
        self.gameTiles[16] = Tile(NoPiece(), 16)
        self.gameTiles[17] = Tile(NoPiece(), 17)
        self.gameTiles[18] = Tile(NoPiece(), 18)
        self.gameTiles[19] = Tile(NoPiece(), 19)
        self.gameTiles[20] = Tile(NoPiece(), 20)
        self.gameTiles[21] = Tile(NoPiece(), 21)
        self.gameTiles[22] = Tile(NoPiece(), 22)
        self.gameTiles[23] = Tile(NoPiece(), 23)
        self.gameTiles[24] = Tile(NoPiece(), 24)
        self.gameTiles[25] = Tile(NoPiece(), 25)
        self.gameTiles[26] = Tile(NoPiece(), 26)
        self.gameTiles[27] = Tile(NoPiece(), 27)
        self.gameTiles[28] = Tile(NoPiece(), 28)
        self.gameTiles[29] = Tile(NoPiece(), 29)
        self.gameTiles[30] = Tile(NoPiece(), 30)
        self.gameTiles[31] = Tile(NoPiece(), 31)
        self.gameTiles[32] = Tile(NoPiece(), 32)
        self.gameTiles[33] = Tile(NoPiece(), 33)
        self.gameTiles[34] = Tile(NoPiece(), 34)
        self.gameTiles[35] = Tile(NoPiece(), 35)
        self.gameTiles[36] = Tile(NoPiece(), 36)
        self.gameTiles[37] = Tile(NoPiece(), 37)
        self.gameTiles[38] = Tile(NoPiece(), 38)
        self.gameTiles[39] = Tile(NoPiece(), 39)
        self.gameTiles[40] = Tile(NoPiece(), 40)
        self.gameTiles[41] = Tile(NoPiece(), 41)
        self.gameTiles[42] = Tile(NoPiece(), 42)
        self.gameTiles[43] = Tile(NoPiece(), 43)
        self.gameTiles[44] = Tile(NoPiece(), 44)
        self.gameTiles[45] = Tile(NoPiece(), 45)
        self.gameTiles[46] = Tile(NoPiece(), 46)
        self.gameTiles[47] = Tile(NoPiece(), 47)
        self.gameTiles[48] = Tile(Pawn("White", 48), 48)
        self.gameTiles[49] = Tile(Pawn("White", 49), 49)
        self.gameTiles[50] = Tile(Pawn("White", 50), 50)
        self.gameTiles[51] = Tile(Pawn("White", 51), 51)
        self.gameTiles[52] = Tile(Pawn("White", 52), 52)
        self.gameTiles[53] = Tile(Pawn("White", 53), 53)
        self.gameTiles[54] = Tile(Pawn("White", 54), 54)
        self.gameTiles[55] = Tile(Pawn("White", 55), 55)
        self.gameTiles[56] = Tile(Rook("White", 56), 56)
        self.gameTiles[57] = Tile(Knight("White", 57), 57)
        self.gameTiles[58] = Tile(Bishop("White", 58), 58)
        self.gameTiles[59] = Tile(Queen("White", 59), 59)
        self.gameTiles[60] = Tile(King("White", 60), 60)
        self.gameTiles[61] = Tile(Bishop("White", 61), 61)
        self.gameTiles[62] = Tile(Knight("White", 62), 62)
        self.gameTiles[63] = Tile(Rook("White", 63), 63)

    def print_board(self):
        count = 0
        for tile in range(64):
            print("|", end=self.gameTiles[tile].pieceOnTile.to_string())
            count += 1
            if count == 8:
                print("|", end='\n')
                count = 0

    def load_board_from_file_path(self, path):
        count = 0
        with open(path) as board_loaded:
            for line in board_loaded:
                for char in line:
                    if char != '|' and char != '\n':
                        if char == '-':
                            self.gameTiles[count] = Tile(NoPiece(), count)
                            count += 1
                        if char == 'R':
                            self.gameTiles[count] = Tile(Rook("Black", count), count)
                            count += 1
                        if char == 'N':
                            self.gameTiles[count] = Tile(Knight("Black", count), count)
                            count += 1
                        if char == 'B':
                            self.gameTiles[count] = Tile(Bishop("Black", count), count)
                            count += 1
                        if char == 'Q':
                            self.gameTiles[count] = Tile(Queen("Black", count), count)
                            count += 1
                        if char == 'K':
                            self.gameTiles[count] = Tile(King("Black", count), count)
                            count += 1
                        if char == 'P':
                            self.gameTiles[count] = Tile(Pawn("Black", count), count)
                            count += 1
                        if char == 'r':
                            self.gameTiles[count] = Tile(Rook("White", count), count)
                            count += 1
                        if char == 'n':
                            self.gameTiles[count] = Tile(Knight("White", count), count)
                            count += 1
                        if char == 'b':
                            self.gameTiles[count] = Tile(Bishop("White", count), count)
                            count += 1
                        if char == 'q':
                            self.gameTiles[count] = Tile(Queen("White", count), count)
                            count += 1
                        if char == 'k':
                            self.gameTiles[count] = Tile(King("White", count), count)
                            count += 1
                        if char == 'p':
                            self.gameTiles[count] = Tile(Pawn("White", count), count)
                            count += 1
        print("Done copying from file")
