from settings import *
import math
from tetromino import Tetromino

class Tetris:
    # input of constructor is application instance
    def __init__(self, app):
        self.app = app
        self.sprite_group = pg.sprite.Gro