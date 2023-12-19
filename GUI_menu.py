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

# font = pygame.font.SysFont("Arial", 32)

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
play_button_menu = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((20, 220), (120, 50)), text="Solve", manager=menu_manager)

# dropdown menus for inital settings
algorithms = ["DFS", "Greedy"]
dropdown_menu_algorithms = pygame_gui.elements.UIDropDownMenu(relative_rect=pygame.Rect((420, 30), (100, 50)), options_list=algorithms, starting_option=algorithms[0], manager=menu_manager)
selected_algorithm = algorithms[1]

algorithm_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((410, 0), (150, 50)), text="Select Algorithm", manager=menu_manager)

sizes= ["2x3", "5x5"]
dropdown_menu_sizes = pygame_gui.elements.UIDropDownMenu(relative_rect=pygame.Rect((20, 30), (100, 50)), options_list=sizes, starting_option=sizes[0], manager=menu_manager)
size = sizes[1]
rows=2
cols=3
# boardindex=random.randint(0,4)

sizes_label= pygame_gui.elements.UILabel(relative_rect=pygame.Rect((0, 0), (150, 50)), text="Select Size", manager=menu_manager)

boardIndexes = ['0','1','2','3','4']
dropdown_menu_boardindexes = pygame_gui.elements.UIDropDownMenu(relative_rect=pygame.Rect((220, 30), (100, 50)), options_list=boardIndexes, starting_option=boardIndexes[0], manager=menu_manager)
boardindex=0

boardIndexes_label= pygame_gui.elements.UILabel(relative_rect=pygame.Rect((200, 0), (150, 50)), text="Select Board", manager=menu_manager)

initial_board = GameBoard.GameBoard(rows, cols, boardindex)

def draw_board(board,window):
    # window.fill(black)
    for row in range(board.rows):
        for col in range(board.cols):
            x = 800 // 2 - board.cols * 50// 2 + col * 50
            y = 600 // 2 - board.rows * 50 // 2 + row * 50+20
            if board.board[row][col] == 1:
                pygame.draw.rect(window, yellow, (x, y, rect_width, rect_height))
            else:
                pygame.draw.rect(window, grey, (x, y, rect_width, rect_height))


def draw_board_initial_board(board,window):
    window.fill(black)
    for row in range(board.rows):
        for col in range(board.cols):
            x = 800 // 2 - board.cols * 50// 2 + col * 50
            y = 600 // 2 - board.rows * 50 // 2 + row * 50+20
            if board.board[row][col] == 1:
                pygame.draw.rect(window, yellow, (x, y, rect_width, rect_height))
            else:
                pygame.draw.rect(window, grey, (x, y, rect_width, rect_height))



draw_board(initial_board,menu_window)
def showing_the_solving(rows,cols,boardindex,algorithm):
    print(rows,cols,boardindex,algorithm)

    white = (255, 255, 255)
    window_width = 800
    window_height = 600
    sleep_time = 0.5


    pygame.init()
    menu_window = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("Zadanie2_Laki_Cmil")

    menu_manager = pygame_gui.UIManager((window_width, window_height))

    font = pygame.font.SysFont("Arial", 20)

    play_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((10, 20), (100, 50)), text="Solve",
                                               manager=menu_manager)
    pause_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((10, 120), (100, 50)), text="Pause",
                                                manager=menu_manager)
    slider = pygame_gui.elements.UIHorizontalSlider(relative_rect=pygame.Rect((10, 220), (100, 50)), start_value=0.5,
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

    # write solver.get_num_moves() as text on the screen
    moves_text = font.render(f"Number of moves: {solver.get_num_moves()}", True, white)
    menu_window.blit(moves_text, (280, 40))
    # write solver.get_num_expanded_states() as text on the screen
    expanded_text = font.render(f"Number of expanded states: {solver.get_num_expanded_states()}", True, white)
    menu_window.blit(expanded_text, (280, 70))
    # write solver.get_time() as text on the screen
    time_text = font.render(f"Time: {round(solver.get_time(),4)} seconds", True, white)
    menu_window.blit(time_text, (280, 100))

    which_board = font.render(f"Board number : {boardindex}", True, white)
    menu_window.blit(which_board, (280, 10))


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
                # remove all from window so windows is blank
                menu_window.fill(black)

            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == play_button:
                        pause = False
                    if event.ui_element == pause_button:
                        pause = True
                if event.user_type == pygame_gui.UI_HORIZONTAL_SLIDER_MOVED:
                    if event.ui_element == slider:
                        sleep_time = slider.get_current_value()



            menu_manager.process_events(event)

        # update the GUI
        menu_manager.update(time_delta)

        # draw the GUI
        menu_manager.draw_ui(menu_window)
        # print(boardindex)
        # draw the board
        # livemove_text = font.render(f"Moves: {solution_index}", True, white)
        # menu_window.blit(livemove_text, (300, 120))
        draw_board(solution[solution_index], menu_window)


        # draw_board(greedySolution[greedySolution_index], len(greedySolver.get_moves()), greedySolver.solved)
        # update the display
        pygame.display.update()

        if not pause:
            time.sleep(sleep_time)
            solution_index += 1
            if solution_index >= len(solution):
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
                    # print(rows,cols)
                    # print(boardindex)
                    # print(selected_algorithm)
                    # time.sleep(3)
                    showing_the_solving(rows,cols,boardindex,selected_algorithm)
                    # menu_window.fill(black)
                    # running = False
            if event.user_type == pygame_gui.UI_DROP_DOWN_MENU_CHANGED:
                if event.ui_element == dropdown_menu_algorithms:
                    selected_algorithm = dropdown_menu_algorithms.selected_option
                    if selected_algorithm == "DFS":
                        print("dfs")
                    elif selected_algorithm == "Greedy":
                        print("greedy")
                    draw_board_initial_board(GameBoard.GameBoard(rows, cols, boardindex), menu_window)

                elif event.ui_element == dropdown_menu_sizes:
                    size = dropdown_menu_sizes.selected_option
                    if size == "2x3":
                        cols = 3
                        rows = 2
                        # boardindex=random.randint(0,4)
                        print("2x3")
                    elif size == "5x5":
                        cols = 5
                        rows = 5
                        # boardindex=random.randint(0,4)
                        print("5x5")
                    draw_board_initial_board(GameBoard.GameBoard(rows, cols, boardindex), menu_window)

                elif event.ui_element == dropdown_menu_boardindexes:
                    boardindex_string = dropdown_menu_boardindexes.selected_option
                    if boardindex_string == "0":
                        boardindex = 0
                    elif boardindex_string == "1":
                        boardindex = 1
                    elif boardindex_string == "2":
                        boardindex = 2
                    elif boardindex_string == "3":
                        boardindex = 3
                    elif boardindex_string == "4":
                        boardindex = 4

                    # print(boardindex)
                    draw_board_initial_board(GameBoard.GameBoard(rows, cols, boardindex), menu_window)
        menu_manager.process_events(event)
    menu_manager.update(time_delta)
    menu_manager.draw_ui(menu_window)
    pygame.display.update()


