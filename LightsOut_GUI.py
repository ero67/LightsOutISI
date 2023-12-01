import pygame
import time
import LightsOut_zadanie
import pygame_gui # import pygame_gui

# initialize the board
initial_board = LightsOut_zadanie.GameBoard(2, 4)

pygame.init()
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Lights Out")

# pygame.display.set_icon(icon)

black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
font = pygame.font.SysFont("Arial", 32)

yellow = (255, 255, 0)
grey = (128, 128, 128)
rect_width = 50
rect_height = 50

# create a UIManager object
manager = pygame_gui.UIManager((window_width, window_height))

# create a button that starts the simulation
start_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((50, 50), (100, 50)),
                                            text='Start',
                                            manager=manager)

# create a slider that changes the speed of the simulation
speed_slider = pygame_gui.elements.UIHorizontalSlider(relative_rect=pygame.Rect((50, 150), (100, 50)),
                                            start_value=0.5,
                                            value_range=(0.1, 1.0),
                                            manager=manager)

# create a label that shows the speed value
speed_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((50, 200), (100, 50)),
                                          text=f'Speed: {speed_slider.get_current_value()}',
                                          manager=manager)

# create a variable to store the sleep time
sleep_time = speed_slider.get_current_value()

# create a button that pauses or resumes the simulation
pause_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((50, 250), (100, 50)),
                                            text='Pause',
                                            manager=manager)

# create a variable to store the pause state
pause = False

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
    window.blit(moves_text, (10, 10))
    if solved:
        status_text = font.render("Solved!", True, green)
    else:
        status_text = font.render("Unsolved", True, red)
    window.blit(status_text, (window_width - status_text.get_width() - 10, 10))
    pygame.display.update()


def show_solution():
    global sleep_time # use the global variable for sleep time
    global pause # use the global variable for pause
    running = True
    solver = LightsOut_zadanie.LightsOutSolver(initial_board)
    solver.solve_dfs()
    solution = solver.get_moves()
    solution_index = 0
    start = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # handle pygame_gui events
            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == start_button:
                        # start the simulation
                        solution_index = 0
                        start = True
                    if event.ui_element == pause_button:
                        # pause or resume the simulation
                        pause = not pause
                        if pause:
                            pause_button.set_text('Resume')
                        else:
                            pause_button.set_text('Pause')
                if event.user_type == pygame_gui.UI_HORIZONTAL_SLIDER_MOVED:
                    if event.ui_element == speed_slider:
                        # update the sleep time and the label
                        sleep_time = speed_slider.get_current_value()
                        speed_label.set_text(f'Speed: {sleep_time}')

            # update the manager
            manager.process_events(event)

            # if start and not pause:
            # draw the current state in the solution
        draw_board(solution[solution_index], len(solver.get_moves()), solver.solved)
            # wait for the sleep time
        time.sleep(sleep_time)
            # increment the solution index
        solution_index += 1

            # if the solution index reaches the end of the solution, reset it to zero
        if solution_index == len(solution):
            solution_index = 0
            break
            # update and draw the manager
        manager.update(1 / 120)
        manager.draw_ui(window)
            # update the display
        pygame.display.update()

def main_loop():
    program_running = True

    while program_running:
        show_solution()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                program_running = False
                break

    pygame.quit()


if __name__ == "__main__":
    main_loop()




# import pygame
# import time
# import LightsOut_zadanie
# import pygame_gui
#
# # initialize the board
# initial_board = LightsOut_zadanie.GameBoard(2, 4)
#
#
#
# pygame.init()
# window_width = 800
# window_height = 600
# window = pygame.display.set_mode((window_width, window_height))
# pygame.display.set_caption("Lights Out")
#
# # pygame.display.set_icon(icon)
#
#
# black = (0, 0, 0)
# white = (255, 255, 255)
# green = (0, 255, 0)
# red = (255, 0, 0)
# font = pygame.font.SysFont("Arial", 32)
#
# yellow = (255, 255, 0)
# grey = (128, 128, 128)
# rect_width = 50
# rect_height = 50
#
#
#
#
# def draw_board(board, moves, solved):
#     window.fill(black)
#     for row in range(board.rows):
#         for col in range(board.cols):
#             x = window_width // 2 - board.cols * rect_width // 2 + col * rect_width
#             y = window_height // 2 - board.rows * rect_height // 2 + row * rect_height
#             if board.board[row][col] == 1:
#                 pygame.draw.rect(window, yellow, (x, y, rect_width, rect_height))
#             else:
#                 pygame.draw.rect(window, grey, (x, y, rect_width, rect_height))
#     moves_text = font.render(f"Moves: {moves}", True, white)
#     window.blit(moves_text, (10, 10))
#     if solved:
#         status_text = font.render("Solved!", True, green)
#     else:
#         status_text = font.render("Unsolved", True, red)
#     window.blit(status_text, (window_width - status_text.get_width() - 10, 10))
#     pygame.display.update()
#
#
# def show_solution():
#     running = True
#     solver = LightsOut_zadanie.LightsOutSolver(initial_board)
#     solver.solve_dfs()
#     solution = solver.get_moves()
#     solution_index = 0
#
#     while running:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False
#         # draw the current state in the solution
#         draw_board(solution[solution_index], len(solver.get_moves()), solver.solved)
#         # wait for one second
#         # time.sleep(0.5)
#         # increment the solution index
#         solution_index += 1
#
#         # if the solution index reaches the end of the solution, reset it to zero
#         if solution_index == len(solution):
#             solution_index = 0
#             break
#
#
# def main_loop():
#     program_running = True
#
#     while program_running:
#         show_solution()
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 program_running = False
#                 break
#
#     pygame.quit()
#
#
# if __name__ == "__main__":
#     main_loop()

#
#
# pygame.init()
# pygame.display.set_caption('Lights Out')
# window_surface = pygame.display.set_mode((1024, 768))
#
# background = pygame.Surface((1024, 768))
# background.fill(pygame.Color('#ADD8E6'))
#
# manager = pygame_gui.UIManager((1024, 768))
#
#
# font = pygame.font.SysFont("Arial", 72)
# text = font.render("LIGHTS OUT", True, (255, 255, 255), (0, 0, 0))
# text_rect = text.get_rect()
# text_rect.center = (100, 100)
#
# window_surface.blit(text,(50,50))
#
#
# label = pygame_gui.elements.UILabel (relative_rect=pygame.Rect((100,50),(200,50)), text = "Select algorithm", manager=manager)
#
# dropdown_menu = pygame_gui.elements.UIDropDownMenu(relative_rect=pygame.Rect((100, 100), (200, 50)),
#                                                    options_list=["DFS", "Greedy", "A*"],
#                                                    starting_option="DFS",
#                                                    manager=manager)
#
# label = pygame_gui.elements.UILabel (relative_rect=pygame.Rect((100,200),(200,50)), text = "Simulation speed", manager=manager)
#
# slider = pygame_gui.elements.UIHorizontalSlider(relative_rect=pygame.Rect((100,250),(200,50)),
#                                                 start_value = 0.5,
#                                                 value_range=[0.5, 1])
#
#
#
#
#
# clock = pygame.time.Clock()
# running = True
# pygame.display.flip()
# while running:
#     # get the time delta
#     time_delta = clock.tick(60) / 1000.0
#
#     # handle events
#     for event in pygame.event.get():
#
#         # if the user wants to quit
#         if event.type == pygame.QUIT:
#             # stop the main loop
#             running = False
#         pygame.display.flip()
#
#         # if the user selects an option from the dropdown menu
#         if event.type == pygame.USEREVENT:
#             if event.user_type == pygame_gui.UI_DROP_DOWN_MENU_CHANGED:
#                 # get the selected option
#                 selected_option = dropdown_menu.selected_option
#                 # print the selected option
#                 print(selected_option)
#
#         if event.type == pygame.USEREVENT:
#             if event.user_type == pygame_gui.UI_HORIZONTAL_SLIDER_MOVED:
#                 value = slider.current_value
#                 print(value)
#
#         # pass the event to the user interface manager
#         manager.process_events(event)
#
#     # update the user interface manager
#     manager.update(time_delta)
#
#     # clear the window
#     window_surface.fill(pygame.Color('#00008b'))
#
#     # draw the user interface
#     manager.draw_ui(window_surface)
#
#     # update the display
#     pygame.display.update()
#
