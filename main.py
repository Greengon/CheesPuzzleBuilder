import pygame
from Board.ChessBoard import ChessBoard
from Board.Move import Move


# Constants
CONSTANT_PIXEL_SIZE = 75
# Constants

# ############## Game Functions ################

def squares(x, y, w, h, color):
    pygame.draw.rect(gameDisplay, color, [x, y, w, h])
    allTiles.append([color, [x, y, w, h]])


def draw_chess_pieces():
    xpos = 0
    ypos = 0
    color = 0
    width = CONSTANT_PIXEL_SIZE
    height = CONSTANT_PIXEL_SIZE
    black = (20, 90, 19)
    white = (250, 250, 200)
    number = 0

    for _ in range(8):
        for _ in range(8):
            if color % 2 == 0:
                squares(xpos, ypos, width, height, white)
                if not chessBoard.gameTiles[number].pieceOnTile.to_string() == '-':
                    img = pygame.image.load("./ChessArt/"
                                            + chessBoard.gameTiles[number].pieceOnTile.alliance[0].lower()
                                            + chessBoard.gameTiles[number].pieceOnTile.to_string().upper()
                                            + ".png")
                    img = pygame.transform.scale(img, (CONSTANT_PIXEL_SIZE, CONSTANT_PIXEL_SIZE))
                    allPieces.append([img, [xpos, ypos], chessBoard.gameTiles[number].pieceOnTile])
                xpos += CONSTANT_PIXEL_SIZE
            else:
                squares(xpos, ypos, width, height, black)
                if not chessBoard.gameTiles[number].pieceOnTile.to_string() == '-':
                    img = pygame.image.load("./ChessArt/"
                                            + chessBoard.gameTiles[number].pieceOnTile.alliance[0].lower()
                                            + chessBoard.gameTiles[number].pieceOnTile.to_string().upper()
                                            + ".png")
                    img = pygame.transform.scale(img, (CONSTANT_PIXEL_SIZE, CONSTANT_PIXEL_SIZE))
                    allPieces.append([img, [xpos, ypos], chessBoard.gameTiles[number].pieceOnTile])
                xpos += CONSTANT_PIXEL_SIZE
            color += 1
            number += 1
        color += 1
        xpos = 0
        ypos += CONSTANT_PIXEL_SIZE

def createSqParams():
    allSqRanges = []
    xMin = 0
    xMax = CONSTANT_PIXEL_SIZE
    yMin = 0
    yMax = CONSTANT_PIXEL_SIZE
    for _ in range(8):
        for _ in range(8):
            allSqRanges.append([xMin, xMax, yMin, yMax])
            xMin += CONSTANT_PIXEL_SIZE
            xMax += CONSTANT_PIXEL_SIZE
        xMin = 0
        xMax = CONSTANT_PIXEL_SIZE
        yMin += CONSTANT_PIXEL_SIZE
        yMax += CONSTANT_PIXEL_SIZE
    return allSqRanges


def updateChessPieces():
    xpos = 0
    ypos = 0
    number = 0
    new_pieces = []
    for _ in range(8):
        for _ in range(8):
            if not chessBoard.gameTiles[number].pieceOnTile.to_string() == "-":
                img = pygame.image.load("./ChessArt/"
                                        + chessBoard.gameTiles[number].pieceOnTile.alliance[0].lower()
                                        + chessBoard.gameTiles[number].pieceOnTile.to_string().upper()
                                        + ".png")
                img = pygame.transform.scale(img, (CONSTANT_PIXEL_SIZE, CONSTANT_PIXEL_SIZE))
                allPieces.append([img, [xpos, ypos], chessBoard.gameTiles[number].pieceOnTile])
            xpos += CONSTANT_PIXEL_SIZE
            number += 1
        xpos = 0
        ypos += CONSTANT_PIXEL_SIZE
    return new_pieces

# ############## Game Functions ################

# Pygame init commands

pygame.init()
gameDisplay = pygame.display.set_mode((CONSTANT_PIXEL_SIZE*8, CONSTANT_PIXEL_SIZE*8))
pygame.display.set_caption("ChessPuzzleBuilder")
clock = pygame.time.Clock()

# Pygame init commands

# Board init commands
chessBoard = ChessBoard()
chessBoard.create_board()
chessBoard.print_board()
# Board init commands

# All needed variables
quitGame = False
allTiles = []
allPieces = []
selectedPiece = None
allSqParams = createSqParams()  # This var is the position of all tile in relation to the gui in a list
# All needed variables



draw_chess_pieces()


# Pygame game loop until user quit's the game
while not quitGame:

    # Check's if the user quited the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quitGame = True
            pygame.quit()
            quit()

        # Check's if the user selected a tile
        if event.type == pygame.MOUSEBUTTONDOWN:
            if selectedPiece is None:
                mx, my = pygame.mouse.get_pos()
                for piece in range(len(allPieces)):
                    if allPieces[piece][1][0] < mx < allPieces[piece][1][0]+CONSTANT_PIXEL_SIZE:
                        if allPieces[piece][1][1] < my < allPieces[piece][1][1] + CONSTANT_PIXEL_SIZE:
                            selectedPiece = piece
                print(selectedPiece)

        # Fallow the user mouse drag
        if event.type == pygame.MOUSEMOTION and selectedPiece is not None:
            mx, my = pygame.mouse.get_pos()
            allPieces[selectedPiece][1][0] = mx - CONSTANT_PIXEL_SIZE/2
            allPieces[selectedPiece][1][1] = my - CONSTANT_PIXEL_SIZE/2

        # TODO: create drag and drop GUI
        # Check's if the user released the mouse
        if event.type == pygame.MOUSEBUTTONUP:
            try:
                print("Mouse button up")
                print("Selected piece: " + str(selectedPiece))
                theMove = 0
                for mov_destination in range(64):
                    if allSqParams[mov_destination][0] < allPieces[selectedPiece][1][0]+CONSTANT_PIXEL_SIZE/2 < allSqParams[mov_destination][1]:
                        if allSqParams[mov_destination][2] < allPieces[selectedPiece][1][1] + CONSTANT_PIXEL_SIZE/2 < allSqParams[mov_destination][3]:
                            theMove = mov_destination
                allPieces[selectedPiece][1][0] = allSqParams[theMove][0]
                allPieces[selectedPiece][1][1] = allSqParams[theMove][2]

                current_move = Move(chessBoard, allPieces[selectedPiece][2], theMove)
                new_board = current_move.create_new_board()
                if new_board is not False:
                    chessBoard = new_board
                new_pieces = updateChessPieces()
                allPieces = new_pieces

            # TODO: to broad except catch
            except:
                pass
            selectedPiece = None

    # reset board
    gameDisplay.fill((255, 255, 255))

    # redraw tiles
    for info in allTiles:
        pygame.draw.rect(gameDisplay, info[0], info[1])

    # redraw images
    for img in allPieces:
        gameDisplay.blit(img[0], img[1])

    pygame.display.update()
    clock.tick(60)
# Pygame loop until user quit's the game
