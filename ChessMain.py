"""
This is our main driver file. It will be responsible for holding the user input and displaying the current GameState.
"""
import pygame as p
import ChessEngine

WIDTH = HEIGHT = 512 #400 is another option
DIMENSION = 8 #dimension of the chess board is 8x8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15 #for animations
