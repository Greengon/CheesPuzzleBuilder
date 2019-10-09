from Board.Tile import Tile
from Pieces.NoPiece import NoPiece


class ChessBoard:

    gameTiles = {}

    def __init__(self):
        pass

    def create_board(self):
        for tile in range(64):
            self.gameTiles[tile] = Tile(NoPiece(), tile)

    def print_board(self):
        count = 0
        for tile in range(64):
            print("|", end=self.gameTiles[tile].pieceOnTile.to_string())
            count += 1
            if count == 8:
                print("|", end='\n')
                count = 0
