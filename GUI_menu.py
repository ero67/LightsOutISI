import pygame
import pygame_gui
import time
import dfsSolver
import GameBoard
import greedySearch
import random

black = (0, 0, 0)
white = (255, 255, 255)
grey = (128, 128, 128)
yellow = (255, 255, 0)
green = (0, 255, 0)
red = (255, 0, 0)

window_width = 800
window_height = 600
rect_width = 50
rect_height = 50
sleep_time = 0.5

pygame.init()
menu_window= pygame.display.set_mode((window_width,window_height))
pygame.display.set_caption("Zadanie2_Laki_Cmil")

menu_manager = pygame_gui.UIManager((window_width, window_height))

# create the GUI elements for menu
play_button_menu = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((10, 300), (100, 50)), text="Solve", manager=menu_manager)

# dropdown menus for inital settings
algorithms = ["DFS", "Greedy"]
dropdown_menu_algorithms = pygame_gui.elements.UIDropDownMenu(relative_rect=pygame.Rect((10, 100), (100, 50)), options_list=algorithms, starting_option=algorithms[0], manager=menu_manager)
selected_algorithm = algorithms[0]

sizes= ["2x3", "5x5"]
dropdown_menu_sizes = pygame_gui.elements.UIDropDownMenu(relative_rect=pygame.Rect((10, 10), (100, 50)), options_list=sizes, starting_option=sizes[0], manager=menu_manager)
size = sizes[0]
rows=2
cols=3
boardindex=random.randint(0,4)


def draw_board(board,window):
    # window.fill(black)
    for row in range(board.rows):
        for col in range(board.cols):
            x = 800 // 2 - board.cols * 50// 2 + col * 50
            y = 600 // 2 - board.rows * 50 // 2 + row * 50
            if board.board[row][col] == 1:
                pygame.draw.rect(window, yellow, (x, y, rect_width, rect_height))
            else:
                pygame.draw.rect(window, grey, (x, y, rect_width, rect_height))
    # moves_text = font.render(f"Moves:   ", True, white)


def showing_the_solving(rows,cols,boardindex,algorithm):
    black = (0, 0, 0)
    white = (255, 255, 255)
    grey = (128, 128, 128)
    yellow = (255, 255, 0)
    green = (0, 255, 0)
    red = (255, 0, 0)

    window_width = 800
    window_height = 600
    rect_width = 50
    rect_height = 50
    sleep_time = 0.5

    pygame.init()
    menu_window = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("Zadanie2_Laki_Cmil")

    menu_manager = pygame_gui.UIManager((window_width, window_height))



    play_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((10, 300), (100, 50)), text="Solve",
                                               manager=menu_manager)
    pause_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((10, 360), (100, 50)), text="Pause",
                                                manager=menu_manager)
    slider = pygame_gui.elements.UIHorizontalSlider(relative_rect=pygame.Rect((10, 420), (100, 50)), start_value=0.5,
                                                    value_range=(1, 0.1), manager=menu_manager)

    # dropdown menus for inital settings

    initial_board = GameBoard.GameBoard(rows, cols, boardindex)
    if algorithm == "DFS":
        solver = dfsSolver.LightsOutSolver_DFS(initial_board)
        solver.solve_dfs()
        solution = solver.get_moves()
    elif algorithm == "Greedy":
        solver = greedySearch.greedySearchSolver(initial_board)
        solver.solve_greedy()
        solution = solver.get_moves()

    solution_index = 0
    # defining if dfs or greedy
    is_dfs = False
    is_greedy = False

    clock = pygame.time.Clock()
    pause = True

    running = True
    clock = pygame.time.Clock()
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



            menu_manager.process_events(event)

        # update the GUI
        menu_manager.update(time_delta)

        # draw the GUI
        menu_manager.draw_ui(menu_window)
        print(boardindex)
        # draw the board
        draw_board(solution[solution_index], menu_window)
        # moves_text = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((500, 10), (100, 50)),
        #                                          text=f"Moves: {moves - 1}", manager=manager)

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
                pause = True
                solution_index = len(solution) - 1
                if is_dfs:
                    is_dfs = False
                if is_greedy:
                    is_greedy = False
                print("tu to konci")



running = True
clock = pygame.time.Clock()
while running:
    time_delta = clock.tick(60) / 1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == play_button_menu:
                    selected_algorithm = dropdown_menu_algorithms.selected_option
                    size = dropdown_menu_sizes.selected_option
                    print(rows,cols)
                    print(boardindex)
                    showing_the_solving(rows,cols,boardindex,selected_algorithm)
                    running = False
            if event.user_type == pygame_gui.UI_DROP_DOWN_MENU_CHANGED:
                if event.ui_element == dropdown_menu_algorithms:
                    selected_algorithm = dropdown_menu_algorithms.selected_option
                    if selected_algorithm == "DFS":
                        print("dfs")
                    elif selected_algorithm == "Greedy":
                        print("greedy")
                elif event.ui_element == dropdown_menu_sizes:
                    size = dropdown_menu_sizes.selected_option
                    if size == "2x3":
                        cols = 3
                        rows = 2
                        boardindex=random.randint(0,4)
                        print("2x3")
                    elif size == "5x5":
                        cols = 5
                        rows = 5
                        boardindex=random.randint(0,4)
                        print("5x5")
        menu_manager.process_events(event)
    menu_manager.update(time_delta)
    menu_manager.draw_ui(menu_window)
    pygame.display.update()


