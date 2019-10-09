import pygame
from Board.ChessBoard import ChessBoard

pygame.init()
gameDisplay = pygame.display.set_mode((600, 600))
pygame.display.set_caption("ChessPuzzleBuilder")
clock = pygame.time.Clock()

chessBoard = ChessBoard()
chessBoard.create_board()
chessBoard.print_board()

quitGame = False
allTiles = []
allPieces = []

# ############## Functions ################


def squares(x, y, w, h, color):
    pygame.draw.rect(gameDisplay, color, [x, y, w, h])
    allTiles.append([color, [x, y, w, h]])


def draw_chess_pieces():
    xpos = 0
    ypos = 0
    color = 0
    width = 75
    height = 75
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
                    img = pygame.transform.scale(img, (75, 75))
                    allPieces.append([img, [xpos, ypos], chessBoard.gameTiles[number].pieceOnTile])
                xpos += 75
            else:
                squares(xpos, ypos, width, height, black)
                if not chessBoard.gameTiles[number].pieceOnTile.to_string() == '-':
                    img = pygame.image.load("./ChessArt/"
                                            + chessBoard.gameTiles[number].pieceOnTile.alliance[0].lower()
                                            + chessBoard.gameTiles[number].pieceOnTile.to_string().upper()
                                            + ".png")
                    img = pygame.transform.scale(img, (75, 75))
                    allPieces.append([img, [xpos, ypos], chessBoard.gameTiles[number].pieceOnTile])
                xpos += 75

            color += 1
            number += 1
        color += 1
        xpos = 0
        ypos += 75

# ############## Functions ################


draw_chess_pieces()


while not quitGame:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            quitGame = True
            pygame.quit()
            quit()

    for img in allPieces:
        gameDisplay.blit(img[0], img[1])

    pygame.display.update()
    clock.tick(60)
