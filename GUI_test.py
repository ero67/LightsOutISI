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

# some initial values

# Initializing the window

window_width = 800
window_height = 600
rect_width = 50
rect_height = 50
sleep_time = 0.5

pygame.init()
window = pygame.display.set_mode((window_width,window_height))
pygame.display.set_caption("Zadanie2_Laki_Cmil")
font = pygame.font.SysFont("Arial", 32)

# manager for pygame_gui library
manager = pygame_gui.UIManager((window_width, window_height))



