from settings import *
from tetris import Tetris
import sys

class App:
    def __init__(self):
        # initialize the window and set a clock in order to update the game
        pg.init()
        pg.display.set_capti