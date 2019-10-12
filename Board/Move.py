import copy
from Board.ChessBoard import ChessBoard
from Board.Tile import Tile


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
            gameTiles[tile] = self.board.gameTiles[tile]

        update_piece = copy.copy(self.movedPiece)
        update_piece.position = self.destination
        gameTiles[self.destination] = Tile(self.destination, update_piece)
        newBoard.gameTiles = gameTiles

        return newBoard
