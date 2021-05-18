from Pieces.NoPiece import NoPiece
from Pieces.Bishop import Bishop
from Pieces.King import King
from Pieces.Knight import Knight
from Pieces.Pawn import Pawn
from Pieces.Queen import Queen
from Pieces.Rook import Rook


class ChessBoard:
    """
    This class represent the board itself.
    It is build off tiles object and game pieces
    objects when the pieces are set
    """

    game_tiles = []
    original_game_tiles = []

    """
    All classes have function called __init__(), which is always 
    executed when the class is being initiated.
    
    Use the __init__() function to assign values to objects properties,
    or other operations that are necessary to do when the object is
    being created.
    """
    def __init__(self):
        self.game_tiles.insert(0, Rook("Black", 0))
        self.game_tiles.insert(1, Knight("Black", 1))
        self.game_tiles.insert(2, Bishop("Black", 2))
        self.game_tiles.insert(3, Queen("Black", 3))
        self.game_tiles.insert(4, King("Black", 4))
        self.game_tiles.insert(5, Bishop("Black", 5))
        self.game_tiles.insert(6, Knight("Black", 6))
        self.game_tiles.insert(7, Rook("Black", 7))
        for i in range(8, 16):
            self.game_tiles.insert(i, Pawn("Black", i))
        for i in range(16, 48):
            self.game_tiles.insert(i, NoPiece(i))
        for i in range(48, 56):
            self.game_tiles.insert(i, Pawn("White", i))
        self.game_tiles.insert(56, Rook("White", 56))
        self.game_tiles.insert(57, Knight("White", 57))
        self.game_tiles.insert(58, Bishop("White", 58))
        self.game_tiles.insert(59, Queen("White", 59))
        self.game_tiles.insert(60, King("White", 60))
        self.game_tiles.insert(61, Bishop("White", 61))
        self.game_tiles.insert(62, Knight("White", 62))
        self.game_tiles.insert(63, Rook("White", 63))
        self.original_game_tiles = self.game_tiles.copy()

    # Testing function only
    def test_print_board(self):
        count = 0
        for tile in range(64):
            print("|", end=self.game_tiles[tile].to_string())
            count += 1
            if count == 8:
                print("|", end='\n')
                count = 0

    def load_board_from_file_path(self, path):
        """
        Load a chess board from .txt file on the local computer.
        :param path: The path to the .txt file.
        :return: None
        """
        count = 0
        with open(path) as board_loaded:
            for line in board_loaded:
                for char in line:
                    if char != '|' and char != '\n':
                        if char == '-':
                            self.game_tiles[count] = NoPiece(count)
                            count += 1
                        if char == 'R':
                            self.game_tiles[count] = Rook("Black", count)
                            count += 1
                        if char == 'N':
                            self.game_tiles[count] = Knight("Black", count)
                            count += 1
                        if char == 'B':
                            self.game_tiles[count] = Bishop("Black", count)
                            count += 1
                        if char == 'Q':
                            self.game_tiles[count] = Queen("Black", count)
                            count += 1
                        if char == 'K':
                            self.game_tiles[count] = King("Black", count)
                            count += 1
                        if char == 'P':
                            self.game_tiles[count] = Pawn("Black", count)
                            count += 1
                        if char == 'r':
                            self.game_tiles[count] = Rook("White", count)
                            count += 1
                        if char == 'n':
                            self.game_tiles[count] = Knight("White", count)
                            count += 1
                        if char == 'b':
                            self.game_tiles[count] = Bishop("White", count)
                            count += 1
                        if char == 'q':
                            self.game_tiles[count] = Queen("White", count)
                            count += 1
                        if char == 'k':
                            self.game_tiles[count] = King("White", count)
                            count += 1
                        if char == 'p':
                            self.game_tiles[count] = Pawn("White", count)
                            count += 1
        self.original_game_tiles = self.game_tiles.copy()
        print("Done copying from file")

    def get_original_tiles(self):
        return self.original_game_tiles

    def set_game_tiles(self, tiles_to_copy):
        self.game_tiles = tiles_to_copy.copy()

    """
    Make a move on the board.
    """
    # TODO: check if it is legal move
    def move(self, moved_piece, destination):
        if moved_piece.position != destination:
            print("moved_piece.position: " + str(moved_piece.position) + " destination: " + str(destination))
            self.game_tiles[moved_piece.position] = NoPiece(moved_piece.position)
            self.game_tiles[destination] = moved_piece
            moved_piece.position = destination
