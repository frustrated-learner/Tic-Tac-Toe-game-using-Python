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
STEEL_BLUE = (70, 130, 180)

# Creating the Main loop of the Game
while RUNNING:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False

    # Filling the Screen with some RGB colors
    SCREEN.fill(LIGHT_STEEL_BLUE)

    # Updating the Dispaly of the Screen
    pygame.display.update()

    # Keeping a Constant Framerate
    CLOCK.tick(60)