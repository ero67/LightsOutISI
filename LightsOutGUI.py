
import pygame
import pygame_gui
import time
import dfsSolver
import GameBoard
import greedySearch

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
# pause = False # initial pause state

# create the pygame window
pygame.init()
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Lights Out Solver")
font = pygame.font.SysFont("Arial", 32)

# create the user interface manager
manager = pygame_gui.UIManager((window_width, window_height))

# create the GUI elements
play_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((10, 300), (100, 50)), text="Solve", manager=manager)
pause_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((10, 360), (100, 50)), text="Pause", manager=manager)
slider = pygame_gui.elements.UIHorizontalSlider(relative_rect=pygame.Rect((10, 420), (100, 50)), start_value=0.5, value_range=(1, 0.1), manager=manager)
slider_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((10, 460), (100, 50)), text="Speed", manager=manager)

# greedybutton=pygame_gui.elements.UIButton(relative_rect=pygame.Rect((10, 340), (100, 50)), text="Greedy", manager=manager)
# dfsbutton=pygame_gui.elements.UIButton(relative_rect=pygame.Rect((10, 400), (100, 50)), text="DFS", manager=manager)

# choose algorithm menu
algorithms = ["DFS", "Greedy"]
dropdown_menu_algorithms = pygame_gui.elements.UIDropDownMenu(relative_rect=pygame.Rect((10, 100), (100, 50)), options_list=algorithms, starting_option=algorithms[0], manager=manager)
selected_algorithm = algorithms[0]


sizes= ["2x3", "5x5"]
dropdown_menu_sizes = pygame_gui.elements.UIDropDownMenu(relative_rect=pygame.Rect((10, 10), (100, 50)), options_list=sizes, starting_option=sizes[0], manager=manager)
size = sizes[0]


# create the initial board
initial_board = GameBoard.GameBoard(2, 3,1)




solver_dfs = dfsSolver.LightsOutSolver_DFS(initial_board)
solver_dfs.solve_dfs()
moves=0

solver_greedy=greedySearch.greedySearchSolver(initial_board)
solver_greedy.solve_greedy()

solution = solver_dfs.get_moves()
solver=solver_dfs
#DFS
# solution = solver.get_moves()


#Greedy
# solution=solver.get_moves()

solution_index = 0

# define a function to draw the board
def draw_board(board, moves, solved,actual_move):
    # window.fill(black)
    for row in range(board.rows):
        for col in range(board.cols):
            x = window_width // 2 - board.cols * rect_width // 2 + col * rect_width
            y = window_height // 2 - board.rows * rect_height // 2 + row * rect_height
            if board.board[row][col] == 1:
                pygame.draw.rect(window, yellow, (x, y, rect_width, rect_height))
            else:
                pygame.draw.rect(window, grey, (x, y, rect_width, rect_height))
    # moves_text = font.render(f"Moves:   ", True, white)




    # pygame.display.update()
    # if solved:
    #     status_text = font.render("Solvable!", True, green)
    # else:
    #     status_text = font.render("Unsolvable", True, red)
    # window.blit(status_text, (window_width - status_text.get_width() - 10, 10))
    # pygame.display.update()

# define the main loop

clock = pygame.time.Clock()
pause=True


#defining if dfs or greedy
is_dfs=False
is_greedy=False

running=False
menu=True
while menu:
    time_delta = clock.tick(60) / 1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            menu = False
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == play_button:
                    menu = False
                    pause = False
                    running = True

    manager.draw_ui(window)


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
                    sleep_time = slider.get_current_value()
            if not is_dfs and not is_greedy:
                if event.user_type == pygame_gui.UI_DROP_DOWN_MENU_CHANGED:
                    if event.ui_element == dropdown_menu_algorithms:
                        selected_algorithm = dropdown_menu_algorithms.selected_option
                        if selected_algorithm == "DFS":
                            solution = solver_dfs.get_moves()
                            solution_index = 0
                            is_dfs=True
                            moves = solver_dfs.get_num_moves()
                            print("dfs")
                        elif selected_algorithm == "Greedy":
                            solution = solver_greedy.get_moves()
                            solution_index = 0
                            moves=solver_greedy.get_num_moves()
                            is_greedy=True
                            print("greedy")
                            # manager.update(time_delta)
                    elif event.ui_element == dropdown_menu_sizes:
                        size = dropdown_menu_sizes.selected_option


        manager.process_events(event)

    # update the GUI
    manager.update(time_delta)

    # draw the GUI
    manager.draw_ui(window)
    # draw the board
    draw_board(solution[solution_index], len(solution), solver.solved,solution_index)
    moves_text = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((500, 10), (100, 50)), text=f"Moves: {moves-1}", manager=manager)

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
            # solution_index = 0
            pause=True
            solution_index=len(solution)-1
            if is_dfs:
                is_dfs=False
            if is_greedy:
                is_greedy=False
            print("tu to konci")

