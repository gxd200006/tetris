from settings import *

class Block(pg.sprite.Sprite):
    def __init__(self, tetromino, pos):
        self.tetromino = tetromino

        super().__init__(tetromin