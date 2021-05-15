from builtins import chr

import pygame
from tkinter.filedialog import askopenfilename
from tkinter import *
from Board.ChessBoard import ChessBoard
from Board.Move import Move


# Constants
CONSTANT_PIXEL_SIZE = 75
# Constants

# ############## Game Functions ################


def squares(x, y, w, h, color, game_display, all_tiles):
    pygame.draw.rect(game_display, color, [x, y, w, h])
    all_tiles.append([color, [x, y, w, h]])


def draw_chess_pieces(game_display,chess_board, all_pieces, all_tiles):
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
                squares(xpos, ypos, width, height, white, game_display, all_tiles)
                if not chess_board.gameTiles[number].pieceOnTile.to_string() == '-':
                    img = pygame.image.load("./ChessArt/"
                                            + chess_board.gameTiles[number].pieceOnTile.alliance[0].lower()
                                            + chess_board.gameTiles[number].pieceOnTile.to_string().upper()
                                            + ".png")
                    img = pygame.transform.scale(img, (CONSTANT_PIXEL_SIZE, CONSTANT_PIXEL_SIZE))
                    all_pieces.append([img, [xpos, ypos], chess_board.gameTiles[number].pieceOnTile])
                xpos += CONSTANT_PIXEL_SIZE
            else:
                squares(xpos, ypos, width, height, black, game_display, all_tiles)
                if not chess_board.gameTiles[number].pieceOnTile.to_string() == '-':
                    img = pygame.image.load("./ChessArt/"
                                            + chess_board.gameTiles[number].pieceOnTile.alliance[0].lower()
                                            + chess_board.gameTiles[number].pieceOnTile.to_string().upper()
                                            + ".png")
                    img = pygame.transform.scale(img, (CONSTANT_PIXEL_SIZE, CONSTANT_PIXEL_SIZE))
                    all_pieces.append([img, [xpos, ypos], chess_board.gameTiles[number].pieceOnTile])
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


def updateChessPieces(chess_board):
    xpos = 0
    ypos = 0
    number = 0
    new_pieces = []
    for x in range(8):
        for y in range(8):
            if not chess_board.gameTiles[number].pieceOnTile.to_string() == "-":
                img = pygame.image.load("./ChessArt/"
                                        + chess_board.gameTiles[number].pieceOnTile.alliance[0].lower()
                                        + chess_board.gameTiles[number].pieceOnTile.to_string().upper()
                                        + ".png")
                img = pygame.transform.scale(img, (CONSTANT_PIXEL_SIZE, CONSTANT_PIXEL_SIZE))
                new_pieces.append([img, [xpos, ypos], chess_board.gameTiles[number].pieceOnTile])
            xpos += CONSTANT_PIXEL_SIZE
            number += 1
        xpos = 0
        ypos += CONSTANT_PIXEL_SIZE
    return new_pieces


# Menu
def game_menu(game_display, chess_board):
    menu = True

    myfont = pygame.font.SysFont("Comic Sans MS", 30)
    menu_title = myfont.render("Welcome", True, (0, 0, 0))
    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 3:
                    print("test")
                    menu = False
        game_display.fill((255, 255, 255))

        # Text
        game_display.blit(menu_title, (100, 50))

        # Button
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if 150 + 100 > mouse[0] > 150 and 450+50 > mouse[1] > 450:
            if click[0] == 1:
                Tk().withdraw()
                filename = askopenfilename()
                chess_board.load_board_from_file_path(filename)
                menu = False
        pygame.draw.rect(game_display, (128, 128, 128), (150, 450, 100, 50))
        button_text = myfont.render("Load", True, (0, 0, 0))
        game_display.blit(button_text, (160, 450))
        pygame.display.update()


# Pygame init commands
def pygame_init_function():
    """
    pygame.init() initialize all imported pygame modules.
    Not all pygame modules need to be initialized, but this will
    automatically initialize the ones that do and saves the trouble of
    manually initializing each module individually.
    :return:
    """
    pygame.init()

    """
    pygame.display -> module to control the display window and screen
        .set_mode() -> Initialize a window or screen for display
        .set_caption() -> Set the current window caption
    """
    game_display = pygame.display.set_mode((CONSTANT_PIXEL_SIZE*8, CONSTANT_PIXEL_SIZE*8))
    pygame.display.set_caption("ChessPuzzleBuilder")

    """
    pygame.time -> Pygame module for monitoring time
        .Clock() -> Create an object to help track time.
    """
    clock = pygame.time.Clock()
    return game_display, clock


def create_and_init_new_board():
    # Board init commands
    chess_board = ChessBoard()
    chess_board.create_board()
    chess_board.print_board()
    return chess_board


# ############## Game Functions ################
# ChessPuzzleBuilder main
def main():
    # init Pygame
    game_display, clock = pygame_init_function()

    # Create new game board
    chess_board = create_and_init_new_board()

    # All needed variables, TODO: Check if needed here
    quit_game = False
    all_tiles = []
    all_pieces = []
    selected_piece = None
    previous_x, previous_y = [0, 0]
    all_squares_parameters = createSqParams()  # This var is the position of all tile in relation to the gui in a list

    game_menu(game_display, chess_board)
    draw_chess_pieces(game_display,chess_board,all_pieces, all_tiles)


    # Pygame game loop until user quit's the game
    while not quit_game:
        click = pygame.mouse.get_pressed()

        # Check's if the user quited the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game = True
                pygame.quit()
                quit()

            # Check's if the user selected a tile
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 2:
                    game_menu()
                    new_pieces = updateChessPieces(chess_board)
                    all_pieces = new_pieces
                if selected_piece is None:
                    mx, my = pygame.mouse.get_pos()
                    for piece in range(len(all_pieces)):
                        if all_pieces[piece][1][0] < mx < all_pieces[piece][1][0] + CONSTANT_PIXEL_SIZE:
                            if all_pieces[piece][1][1] < my < all_pieces[piece][1][1] + CONSTANT_PIXEL_SIZE:
                                selected_piece = piece
                                previous_x = all_pieces[piece][1][0]
                                previous_y = all_pieces[piece][1][1]
                    print(selected_piece)

            # Fallow the user mouse drag
            if event.type == pygame.MOUSEMOTION and selected_piece is not None:
                mx, my = pygame.mouse.get_pos()
                all_pieces[selected_piece][1][0] = mx - CONSTANT_PIXEL_SIZE/2
                all_pieces[selected_piece][1][1] = my - CONSTANT_PIXEL_SIZE/2

            # TODO: create drag and drop GUI
            # Check's if the user released the mouse
            if event.type == pygame.MOUSEBUTTONUP and selected_piece is not None:
                try:
                    print("Mouse button up")
                    print("Selected piece: " + str(selected_piece))
                    theMove = 0
                    for mov_destination in range(64):
                        if all_squares_parameters[mov_destination][0] < all_pieces[selected_piece][1][0]+CONSTANT_PIXEL_SIZE/2 < all_squares_parameters[mov_destination][1]:
                            if all_squares_parameters[mov_destination][2] < all_pieces[selected_piece][1][1] + CONSTANT_PIXEL_SIZE/2 < all_squares_parameters[mov_destination][3]:
                                theMove = mov_destination
                    all_pieces[selected_piece][1][0] = all_squares_parameters[theMove][0]
                    all_pieces[selected_piece][1][1] = all_squares_parameters[theMove][2]

                    current_move = Move(chess_board, all_pieces[selected_piece][2], theMove)
                    new_board = current_move.create_new_board()
                    if new_board is not False:
                        chess_board = new_board
                    new_pieces = updateChessPieces(chess_board)
                    all_pieces = new_pieces
                    chess_board.print_board()

                # TODO: to broad except catch
                except Exception as e:
                    print(e)
                previous_y = 0
                previous_x = 0
                selected_piece = None

        # reset board
        game_display.fill((255, 255, 255))

        # redraw tiles
        for info in all_tiles:
            pygame.draw.rect(game_display, info[0], info[1])

        # redraw images
        for img in all_pieces:
            game_display.blit(img[0], img[1])

        pygame.display.update()
        clock.tick(60)
    # Pygame loop until user quit's the game


# The main app function
if __name__ == '__main__':
    main()

