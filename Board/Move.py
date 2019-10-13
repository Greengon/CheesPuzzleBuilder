import copy
from Board.ChessBoard import ChessBoard
from Board.Tile import Tile
from Pieces.NoPiece import NoPiece


class Move:
    board = None
    movedPiece = None
    destination = None

    def __init__(self, board, moved_piece, destination):
        self.board = board
        self.movedPiece = moved_piece
        self.destination = destination

    def create_new_board(self):
        newBoard = ChessBoard()
        gameTiles = {}

        for tile in range(64):
            if not tile == self.movedPiece.position and not tile == self.destination:
                gameTiles[tile] = self.board.gameTiles[tile]
            else:
                gameTiles[tile] = Tile(NoPiece(), tile)

        update_piece = copy.copy(self.movedPiece)
        update_piece.position = self.destination
        gameTiles[self.destination] = Tile(update_piece, self.destination)
        newBoard.gameTiles = gameTiles

        return newBoard
