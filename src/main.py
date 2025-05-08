from settings import *
from tetris import Tetris
import sys

class App:
    def __init__(self):
        # initialize the window and set a clock in order to update the game
        pg.init()
        pg.display.set_caption("Tetris")
        self.screen = pg.display.set_mode(FIELD_RES)
        self.clock = pg.time.Clock()
        self.tetris = Tetris(self)
    
    def update(self):
        # set the framerate- FPS var created in settings.py
        self.tetris.update()
        self.clock.tick(FPS)
    
    def draw(self):
        # draw & display the background
        self.screen.fill(color=FIELD_COLOR)
        self.tetris.draw()
        pg.display.flip()
    
    def check_events(self):
        # check if user quits the game, and exit accordingly
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
    
    def run(self):
        # main game loop - calls the three methods defined above
        while True:
            self.check_events()
            self.update()
            self.draw()

if __name__ == '__main__':
    app = App()
    app.run()