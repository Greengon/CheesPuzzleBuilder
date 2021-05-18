from tkinter import Tk
from tkinter.filedialog import askopenfilename

import pygame

from GUI.Button import Button


class Toolbar:

    # Attributes
    left_button = None
    right_button = None
    image = None
    rect = None

    def __init__(self, width, height, background_color="Gray"):
        self.image = pygame.Surface((width, height))
        self.image.fill(background_color)
        self.rect = self.image.get_rect()
        self.rect.topleft = (0, 0)
        self.left_button = Button("Restart", (5, 5), 20)
        self.right_button = Button("Load", (100, 5), 20)

    def draw(self, screen):
        # screen.blit("what to print", ("From which x to start", "From which y to start"))
        screen.blit(self.image, (0, 0))
        self.left_button.draw(screen)
        self.right_button.draw(screen)

    def click(self, position, chess_board):
        print("Toolbar clicked")
        if self.left_button.get_rect().collidepoint(position):
            # Restart button
            chess_board.set_game_tiles(chess_board.get_original_tiles())
        elif self.right_button.get_rect().collidepoint(position):
            # Load button
            Tk().withdraw()
            filename = askopenfilename()
            chess_board.load_board_from_file_path(filename)



