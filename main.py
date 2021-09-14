import pygame
import numpy as np

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

# Creating the Variables for the Square
SQUARE_ROW = 3
SQUARE_COLUMN = 3
SQUARE = np.zeros( (SQUARE_ROW, SQUARE_COLUMN) )

# Creating the Variables for the Circle
CIRCLE_RADIUS = 60
CIRCLE_WIDTH = 14

# Creating the Variables for the Player
player = 1

# Creating some Game Variables
GAME_OVER = False

# Colors
LIGHT_STEEL_BLUE = (20, 189, 172)
DARK_STEEL_BLUE = (13, 161, 146)
CIRCLE_COLOR = (242, 235, 211)
CROSS_COLOR = (84, 84, 84)

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

# Creating the Class for the Figures
class FIGURES:
    def __init__(self):
        pass

    # Creating the Function to Draw the Figures on the Screen
    def draw_figures(self):
        for row in range(SQUARE_ROW):
            for column in range(SQUARE_COLUMN):
                # Drawing the Circle
                if SQUARE[row][column] == 1:
                    pygame.draw.circle(SCREEN, CIRCLE_COLOR, (int(row * 200 + 200 / 2), int(column * 200 + 200 / 2)), CIRCLE_RADIUS, CIRCLE_WIDTH)
                # Drawing the Cross
                elif SQUARE[row][column] == 2:
                    pygame.draw.line(SCREEN, CROSS_COLOR, (row * 200 + 200 - 40, column * 200 + 40), (row * 200 + 40, column * 200 + 200 - 40),  14)
                    pygame.draw.line(SCREEN, CROSS_COLOR, (row * 200 + 40, column * 200 + 40), (row * 200 + 200 - 40, column * 200 + 200 - 40),  14)


# Creating the Class for the Main logic of the Game
class MAIN:
    def __init__(self):
        self.lines = LINES()
        self.figures = FIGURES()

    # Creating the Function to Draw the Elements on the Screen
    def draw_elements(self):
        self.lines.draw_vertical_line()
        self.lines.draw_horizontal_line()
        self.figures.draw_figures()
        self.check_win()
        
    # Creating the Function to Mark the Square
    def mark_square(self, row, column, player):
        SQUARE[row][column] = player

    # Creating the Function to Find the Available Square
    def available_square(self, row, column):
        return SQUARE[row][column] == 0

    # Creating the Function to Check if the Board is full
    def is_board_full(self):
        for row in range(SQUARE_ROW):
            for column in range(SQUARE_COLUMN):
                if SQUARE[row][column] == 0:
                    return False
                
        return True

    # Creating the Function to Check if the Player has Won
    def check_win(self):
        global GAME_OVER
        
        # Creating the Condition to Draw the Horizontal Lines
        for column in range(SQUARE_COLUMN):
            if SQUARE[0][column] == 1 and SQUARE[1][column] == 1 and SQUARE[2][column] == 1:
                pygame.draw.line(SCREEN, CIRCLE_COLOR, (column / 1 + 20, column * 200 + 100), (column / 1 + 580, column * 200 + 100), 14)
                GAME_OVER = True
            elif SQUARE[0][column] == 2 and SQUARE[1][column] == 2 and SQUARE[2][column] == 2:
                pygame.draw.line(SCREEN, CROSS_COLOR, (column / 1 + 20, column * 200 + 100), (column / 1 + 580, column * 200 + 100), 14)
                GAME_OVER = True 

        # Creating the Condition to Draw the Vertical Lines
        for row in range(SQUARE_ROW):
            if SQUARE[row][0] == 1 and SQUARE[row][1] == 1 and SQUARE[row][2] == 1:
                pygame.draw.line(SCREEN, CIRCLE_COLOR, (row * 200 + 100, row / 1 + 580), (row * 200 + 100, row / 1 + 20), 14)
                GAME_OVER = True
            elif SQUARE[row][0] == 2 and SQUARE[row][1] == 2 and SQUARE[row][2] == 2:
                pygame.draw.line(SCREEN, CROSS_COLOR, (row * 200 + 100, row / 1 + 580), (row * 200 + 100, row / 1 + 20), 14)
                GAME_OVER = True

        # Creating the Condition to Draw the Backslash Lines
        if SQUARE[0][0] == 1 and SQUARE[1][1] == 1 and SQUARE[2][2] == 1:
            pygame.draw.line(SCREEN, CIRCLE_COLOR, (20, 20), (580, 580), 14)
            GAME_OVER = True
        elif SQUARE[0][0] == 2 and SQUARE[1][1] == 2 and SQUARE[2][2] == 2:
            pygame.draw.line(SCREEN, CROSS_COLOR, (20, 20), (580, 580), 14)
            GAME_OVER = True

        # Creating the Condition to Draw the Forward Slash Lines
        if SQUARE[0][2] == 1 and SQUARE[1][1] == 1 and SQUARE[2][0] == 1:
            pygame.draw.line(SCREEN, CIRCLE_COLOR, (580, 20), (20, 580), 14)
            GAME_OVER = True
        elif SQUARE[0][2] == 2 and SQUARE[1][1] == 2 and SQUARE[2][0] == 2:
            pygame.draw.line(SCREEN, CROSS_COLOR, (580, 20), (20, 580), 14)
            GAME_OVER = True
            
    # Creating the Function to Restart the Game
    def game_reset(self):
        global SQUARE
        global player
        SCREEN.fill(LIGHT_STEEL_BLUE)
        self.lines.draw_vertical_line()
        self.lines.draw_horizontal_line()
        player = 1
        SQUARE_ROW = 3
        SQUARE_COLUMN = 3
        SQUARE = np.zeros( (SQUARE_ROW, SQUARE_COLUMN) )



# Assigning the Classes
main_game = MAIN()


# Creating the Main loop of the Game
while RUNNING:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False

        # Creating the Event to Check the Mouse Button Click
        if event.type == pygame.MOUSEBUTTONDOWN and not GAME_OVER:
            # Adjusting the Clicking Window
            mouse_x = event.pos[0]
            mouse_y = event.pos[1]

            # Creating the Variable for the Mouse Click Axis
            clicked_x = int(mouse_x // 200)
            clicked_y = int(mouse_y // 200)

            # Creating the Condition to Fill the Console Board
            if main_game.available_square(clicked_x, clicked_y):
                if player == 1:
                    main_game.mark_square(clicked_x, clicked_y, player)
                    player = 2
                elif player == 2:
                    main_game.mark_square(clicked_x, clicked_y, player)
                    player = 1
            
        # Creating the Event to Restart the Game
        if (event.type == pygame.KEYDOWN and GAME_OVER) or (event.type == pygame.KEYDOWN and main_game.is_board_full()):
            if event.key == pygame.K_SPACE:
                GAME_OVER = False
                main_game.game_reset()

    # Filling the Screen with some RGB colors
    SCREEN.fill(LIGHT_STEEL_BLUE)

    # Calling the Functions to Draw the Elements on the Screen
    main_game.draw_elements()

    # Updating the Dispaly of the Screen
    pygame.display.update()

    # Keeping a Constant Framerate
    CLOCK.tick(60)