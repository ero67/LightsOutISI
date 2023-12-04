#sws pato

import pygame
import pygame_gui
import time
import dfsSolver
import GameBoard
import greedySearchpomocuz

# define some colors
black = (0, 0, 0)
white = (255, 255, 255)
grey = (128, 128, 128)
yellow = (255, 255, 0)
green = (0, 255, 0)
red = (255, 0, 0)

# define some constants
window_width = 800
window_height = 600
rect_width = 50
rect_height = 50
sleep_time = 0.5 # initial sleep time
pause = False # initial pause state

# create the pygame window
pygame.init()
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Lights Out Solver")
font = pygame.font.SysFont("Arial", 32)

# create the user interface manager
manager = pygame_gui.UIManager((window_width, window_height))

# create the GUI elements
play_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((10, 100), (100, 50)), text="Solve", manager=manager)
pause_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((10, 160), (100, 50)), text="Pause", manager=manager)
slider = pygame_gui.elements.UIHorizontalSlider(relative_rect=pygame.Rect((10, 220), (100, 50)), start_value=0.5, value_range=(0.1, 1.0), manager=manager)
slider_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((10, 280), (100, 50)), text="Speed", manager=manager)

# choose algorithm menu
# algorithms = ["DFS", "Greedy"]
# menu = pygame_gui.elements.UIDropDownMenu(relative_rect=pygame.Rect((10, 10), (100, 50)), options_list=algorithms, starting_option=algorithms[0], manager=manager)
# selected_algorithm = algorithms[0]


# create the initial board
initial_board = GameBoard.GameBoard(3, 3)



# solver = dfsSolver.LightsOutSolver_DFS(initial_board)
# solver.solve_dfs()

solver=greedySearchpomocuz.greedySearchSolver(initial_board)
solver.solve_greedy()
#DFS
# solution = solver.get_moves()


#Greedy
solution=solver.get_moves()

solution_index = 0

# define a function to draw the board
def draw_board(board, moves, solved):
    # window.fill(black)
    for row in range(board.rows):
        for col in range(board.cols):
            x = window_width // 2 - board.cols * rect_width // 2 + col * rect_width
            y = window_height // 2 - board.rows * rect_height // 2 + row * rect_height
            if board.board[row][col] == 1:
                pygame.draw.rect(window, yellow, (x, y, rect_width, rect_height))
            else:
                pygame.draw.rect(window, grey, (x, y, rect_width, rect_height))

    moves_text = font.render(f"Moves: {moves}", True, white)
    window.blit(moves_text, (500, 10))
    if solved:
        status_text = font.render("Solvable!", True, green)
    else:
        status_text = font.render("Unsolvable", True, red)
    window.blit(status_text, (window_width - status_text.get_width() - 10, 10))
    pygame.display.update()

# define the main loop
running = True
clock = pygame.time.Clock()
pause=True

while running:
    # get the time delta
    time_delta = clock.tick(60) / 1000.0

    # handle the events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == play_button:
                    pause = False  # resume the animation
                if event.ui_element == pause_button:
                    pause = True  # pause the animation
            if event.user_type == pygame_gui.UI_HORIZONTAL_SLIDER_MOVED:
                if event.ui_element == slider:
                    sleep_time = slider.get_current_value()  # get the new sleep time from the slider
        manager.process_events(event)

    # update the GUI
    manager.update(time_delta)

    # draw the GUI
    manager.draw_ui(window)

    # draw the board
    draw_board(solution[solution_index], len(solver.get_moves()), solver.solved)
    # draw_board(greedySolution[greedySolution_index], len(greedySolver.get_moves()), greedySolver.solved)
    # update the display
    pygame.display.update()

    # check if the animation is paused
    if not pause:
        # wait for the sleep time
        time.sleep(sleep_time)
        # increment the solution index
        solution_index += 1
        # wrap around the solution index
        if solution_index >= len(solution):
            solution_index = 0
            pause=True

    # if not pause:
    #     # wait for the sleep time
    #     time.sleep(sleep_time)
    #     # increment the solution index
    #     greedySolution_index += 1
    #     # wrap around the solution index
    #     if greedySolution_index >= len(greedySolution):
    #         greedySolution_index = 0
    #         pause=True
