from settings import *
import math

class Tetris:
    # input of constructor is application instance
    def __init__(self, app):
        self.app = app
    
    def draw_grid(self):
        for x in (FIELD_W):
            for y in (FIELD_H):
                pg.draw.rect(self.app.screen, 'white', (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE), 1)
    
    def update(self):
        pass

    def draw(self):
        self.draw_grid()