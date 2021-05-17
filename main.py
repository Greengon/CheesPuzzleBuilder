import pygame
from tkinter.filedialog import askopenfilename
from tkinter import *
from Board.ChessBoard import ChessBoard


# Constants
from GUI.Toolbar import Toolbar

CONSTANT_PIXEL_SIZE = 70    # Normally 75
BLACK = (20, 90, 19)
WHITE = (250, 250, 200)


# ############## Game Functions ################
def square_printing_function(x, y, color, game_display, all_tiles):
    """
    Square printing function.
    :param x: x position
    :param y: y position
    :param w: Width
    :param h: High
    :param color: Color
    :param game_display: The current GUI display
    :param all_tiles: All squares of the board
    :return: None
    """
    pygame.draw.rect(game_display, color, [x, y, CONSTANT_PIXEL_SIZE, CONSTANT_PIXEL_SIZE])
    all_tiles.append([color, [x, y, CONSTANT_PIXEL_SIZE, CONSTANT_PIXEL_SIZE]])


def draw_chess_pieces(game_display, chess_board, all_pieces, all_tiles):
    """
    This function will draw the board for us.
    :param game_display:
    :param chess_board:
    :param all_pieces:
    :param all_tiles:
    :return: None
    """

    # Counters variables
    x_position = CONSTANT_PIXEL_SIZE
    y_position = CONSTANT_PIXEL_SIZE
    color = 0
    number = 0

    for _ in range(8):
        for _ in range(8):
            given_color = WHITE if color % 2 == 0 else BLACK
            square_printing_function(x_position, y_position, given_color, game_display, all_tiles)
            if not chess_board.game_tiles[number].to_string() == '-':
                img = pygame.image.load("./ChessArt/"
                                        + chess_board.game_tiles[number].alliance[0].lower()
                                        + chess_board.game_tiles[number].to_string().upper()
                                        + ".png")
                img = pygame.transform.scale(img, (CONSTANT_PIXEL_SIZE, CONSTANT_PIXEL_SIZE))
                all_pieces.append([img, [x_position, y_position], chess_board.game_tiles[number]])
            x_position += CONSTANT_PIXEL_SIZE
            color += 1
            number += 1
        color += 1
        x_position = CONSTANT_PIXEL_SIZE
        y_position += CONSTANT_PIXEL_SIZE


def create_squares_parameters():
    """
    This functions returns a list in the size of the board
    and for each item it holds the corresponded place in pixels
    of that item on the board in the GUI showed for the user.
    """
    all_squares_ranges = []
    x_min = CONSTANT_PIXEL_SIZE
    x_max = CONSTANT_PIXEL_SIZE * 2
    y_min = CONSTANT_PIXEL_SIZE
    y_max = CONSTANT_PIXEL_SIZE * 2
    for _ in range(8):
        for _ in range(8):
            all_squares_ranges.append([x_min, x_max, y_min, y_max])
            x_min += CONSTANT_PIXEL_SIZE
            x_max += CONSTANT_PIXEL_SIZE
        x_min = CONSTANT_PIXEL_SIZE
        x_max = CONSTANT_PIXEL_SIZE * 2
        y_min += CONSTANT_PIXEL_SIZE
        y_max += CONSTANT_PIXEL_SIZE
    return all_squares_ranges


def print_pieces_images(chess_board):
    x_position = CONSTANT_PIXEL_SIZE
    y_position = CONSTANT_PIXEL_SIZE
    number = 0
    new_pieces = []
    for x in range(8):
        for y in range(8):
            if not chess_board.game_tiles[number].to_string() == "-":
                img = pygame.image.load("./ChessArt/"
                                        + chess_board.game_tiles[number].alliance[0].lower()
                                        + chess_board.game_tiles[number].to_string().upper()
                                        + ".png")
                img = pygame.transform.scale(img, (CONSTANT_PIXEL_SIZE, CONSTANT_PIXEL_SIZE))
                new_pieces.append([img, [x_position, y_position], chess_board.game_tiles[number]])
            x_position += CONSTANT_PIXEL_SIZE
            number += 1
        x_position = CONSTANT_PIXEL_SIZE
        y_position += CONSTANT_PIXEL_SIZE
    return new_pieces


def game_menu(game_display, chess_board):
    """
    Show the user a menu.
    :param game_display: GUI.display object of our game.
    :param chess_board: Our board as an object.
    :return: None
    """

    # Chosen font for the menu
    my_font = pygame.font.SysFont("Comic Sans MS", 28)
    menu_title = my_font.render("Welcome To Green's Chess Puzzle Builder", True, (0, 0, 0))
    load_button_text = my_font.render("Load", True, (0, 0, 0))
    new_game_button_text = my_font.render("New Game", True, (0, 0, 0))
    menu_keep_alive = True
    while menu_keep_alive:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # User chose to quit the game.
                pygame.quit()
                quit()
        game_display.fill((255, 255, 255))

        # Text
        game_display.blit(menu_title, (10, 50))

        # Buttons
        # pygame.draw.rect(game_display, (color, color, color), (x coordinate, y coordinate, width, high))

        # New Game button
        pygame.draw.rect(game_display, (128, 128, 128), (150, 350, 150, 50))
        game_display.blit(new_game_button_text, (160, 350))

        # Load button
        pygame.draw.rect(game_display, (128, 128, 128), (150, 450, 80, 50))
        game_display.blit(load_button_text, (160, 450))

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        # If User pressed on "New Game"
        if 150 + 150 > mouse[0] > 150 and 350+50 > mouse[1] > 350:
            if click[0] == 1:
                menu_keep_alive = False

        # If User pressed on "Load"
        elif 150 + 80 > mouse[0] > 150 and 450+50 > mouse[1] > 450:
            if click[0] == 1:
                Tk().withdraw()
                filename = askopenfilename()
                chess_board.load_board_from_file_path(filename)
                menu_keep_alive = False

        pygame.display.update()


def pygame_init_function():
    """
    Initialize all GUI modules
    :return: pygame display object and pygame.time Clock object.
    """

    """
    pygame.init() initialize all imported pygame modules.
    Not all pygame modules need to be initialized, but this will
    automatically initialize the ones that do and saves the trouble of
    manually initializing each module individually.
    """
    pygame.init()

    """
    pygame.display -> module to control the display window and screen
        .set_mode() -> Initialize a window or screen for display
        .set_caption() -> Set the current window caption
    """
    game_display = pygame.display.set_mode((CONSTANT_PIXEL_SIZE*9, CONSTANT_PIXEL_SIZE*9))
    pygame.display.set_caption("ChessPuzzleBuilder")

    """
    pygame.time -> GUI module for monitoring time
        .Clock() -> Create an object to help track time.
    """
    clock = pygame.time.Clock()
    return game_display, clock


def notation_drawing(game_display):
    """
    Drawing the chess notation on the display
    :param game_display: Game display
    :return: None
    """
    font = pygame.font.SysFont("Arial", 30)
    left_notation_y = 85
    for i in range(0, 8):
        notation = font.render(str(8-i), 1, pygame.Color("White"))
        game_display.blit(notation, (40, left_notation_y))
        left_notation_y += 70
    upside_notation_x = CONSTANT_PIXEL_SIZE + 20
    for i in range(65, 73):
        notation = font.render(chr(i), 1, pygame.Color("White"))
        game_display.blit(notation, (upside_notation_x, 35))
        upside_notation_x += 70


# ############## Game Functions ################
# ChessPuzzleBuilder main
def main():
    # init GUI
    game_display, clock = pygame_init_function()

    # Create new game board object and test print it
    chess_board = ChessBoard()
    chess_board.test_print_board()  # Test function TODO: delete me in the end

    # All needed variables, TODO: Check if needed here
    quit_game = False
    all_tiles = []
    all_pieces = []
    selected_piece = None

    # This var is a list that holds the position in pixels of all tiles in relation to the user GUI
    all_squares_parameters = create_squares_parameters()

    # Show the menu to the user
    game_menu(game_display, chess_board)

    # Board drawing function
    draw_chess_pieces(game_display, chess_board, all_pieces, all_tiles)

    # Create toolbar
    toolbar = Toolbar(CONSTANT_PIXEL_SIZE*9, CONSTANT_PIXEL_SIZE/2, (128, 128, 128))

    # GUI game loop until user quits the game
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
                    new_pieces = print_pieces_images(chess_board)
                    all_pieces = new_pieces
                if selected_piece is None:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    for piece in range(len(all_pieces)):
                        if all_pieces[piece][1][0] < mouse_x < all_pieces[piece][1][0] + CONSTANT_PIXEL_SIZE:
                            if all_pieces[piece][1][1] < mouse_y < all_pieces[piece][1][1] + CONSTANT_PIXEL_SIZE:
                                selected_piece = piece
                    if 0 < mouse_x < CONSTANT_PIXEL_SIZE * 9 and 0 < mouse_y < CONSTANT_PIXEL_SIZE / 2:
                        toolbar.click((mouse_x, mouse_y), chess_board,game_display)
                    print(selected_piece)

            # Fallow the user mouse drag
            if event.type == pygame.MOUSEMOTION and selected_piece is not None:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                all_pieces[selected_piece][1][0] = mouse_x - CONSTANT_PIXEL_SIZE/2
                all_pieces[selected_piece][1][1] = mouse_y - CONSTANT_PIXEL_SIZE/2

            # TODO: create drag and drop GUI
            # Check's if the user released the mouse
            if event.type == pygame.MOUSEBUTTONUP and selected_piece is not None:
                try:
                    print("Mouse button up")
                    print("Selected piece: " + str(selected_piece))
                    the_move = 0
                    for mov_destination in range(64):
                        if all_squares_parameters[mov_destination][0] < all_pieces[selected_piece][1][0] + \
                                CONSTANT_PIXEL_SIZE / 2 < all_squares_parameters[mov_destination][1]:
                            if all_squares_parameters[mov_destination][2] < all_pieces[selected_piece][1][1] + \
                                    CONSTANT_PIXEL_SIZE / 2 < all_squares_parameters[mov_destination][3]:
                                the_move = mov_destination
                    all_pieces[selected_piece][1][0] = all_squares_parameters[the_move][0]
                    all_pieces[selected_piece][1][1] = all_squares_parameters[the_move][2]

                    chess_board.move(all_pieces[selected_piece][2], the_move)
                    all_pieces = print_pieces_images(chess_board)
                    chess_board.test_print_board()  # Test function TODO: delete me in the end

                # TODO: to broad except catch
                except Exception as e:
                    print(e)
                selected_piece = None

        # reset board
        game_display.fill((127, 78, 40))
        toolbar.draw(game_display)
        notation_drawing(game_display)

        # redraw tiles
        for info in all_tiles:
            pygame.draw.rect(game_display, info[0], info[1])

        # redraw images
        for img in all_pieces:
            game_display.blit(img[0], img[1])

        pygame.display.update()
        clock.tick(60)
    # GUI loop until user quit's the game


# The main app function
if __name__ == '__main__':
    main()

