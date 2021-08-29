import pygame

# Initializing the Pygame
pygame.init()

# Creating some Screen Variables
HEIGHT = 600
WIDTH = 600
RUNNING = True
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
ICON = pygame.image.load("icon/icon.png").convert_alpha()
pygame.display.set_caption("Tic Tac Toe")
pygame.display.set_icon(ICON)
CLOCK = pygame.time.Clock()

# Colors
LIGHT_STEEL_BLUE = (20, 189, 172)
DARK_STEEL_BLUE = (13, 161, 146)

# Creating the Class for the Lines
class LINES:
    def __init__(self):
        pass

    # Creating the Function to Draw the Vertical lines
    def draw_vertical_line(self):
        pygame.draw.line(SCREEN, DARK_STEEL_BLUE, (200, 0), (200, 600), 10)
        pygame.draw.line(SCREEN, DARK_STEEL_BLUE, (400, 0), (400, 600), 10)

    # Creating the Function to Draw the Horizontal Lines
    def draw_horizontal_line(self):
        pygame.draw.line(SCREEN, DARK_STEEL_BLUE, (0, 200), (600, 200), 10)
        pygame.draw.line(SCREEN, DARK_STEEL_BLUE, (0, 400), (600, 400), 10)

# Creating the Class for the Main logic of the Game
class MAIN:
    def __init__(self):
        self.lines = LINES()

    # Creating the Function to Draw the Elements on the Screen
    def draw_elements(self):
        self.lines.draw_vertical_line()
        self.lines.draw_horizontal_line()

# Assigning the Classes
main_game = MAIN()


# Creating the Main loop of the Game
while RUNNING:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False

    # Filling the Screen with some RGB colors
    SCREEN.fill(LIGHT_STEEL_BLUE)

    # Calling the Function to Draw the Elements on the Screen
    main_game.draw_elements()

    # Updating the Dispaly of the Screen
    pygame.display.update()

    # Keeping a Constant Framerate
    CLOCK.tick(60)