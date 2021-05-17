import pygame.font


class Button:
    # Attributes
    x = None
    y = None
    font = None
    feedback = ""
    text = ""
    size = None
    surface = None
    rect = None

    def __init__(self, text, position, font, bg=(127, 78, 40), feedback=""):
        self.x, self.y = position
        self.font = pygame.font.SysFont("Arial", font)
        if feedback == "":
            self.feedback = "text"
        else:
            self.feedback = feedback
        self.text = self.font.render(text, 1, pygame.Color("White"))
        self.size = self.text.get_size()
        self.surface = pygame.Surface(self.size)
        self.surface.fill(bg)
        self.surface.blit(self.text, (0, 0))
        self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])

    def get_rect(self):
        return self.rect

    def draw(self, screen):
        screen.blit(self.surface, (self.x, self.y))

    def click(self, event):
        x, y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if self.rect.collidepoint(x, y):
                    print("Button pressed")
