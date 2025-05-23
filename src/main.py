from settings import *
from tetris import Tetris, Text
import sys
import pathlib

class App:
    def __init__(self):
        # initialize the window and set a clock in order to update the game
        pg.init()
        pg.display.set_caption("Tetris")
        self.screen = pg.display.set_mode(WIN_RES)
        self.clock = pg.time.Clock()
        self.set_timer()
        self.images = self.load_images()
        self.tetris = Tetris(self)
        self.text = Text(self)
    
    def load_images(self):
        files = [item for item in pathlib.Path(SPRITE_DIR_PATH).rglob('*.png') if item.is_file()]
        images = [pg.image.load(file).convert_alpha() for file in files]
        images = [pg.transform.scale(image, (TILE_SIZE, TILE_SIZE)) for image in images]
        return images
    
    def set_timer(self):
        self.user_event = pg.USEREVENT + 0
        self.fast_user_event = pg.USEREVENT + 1
        self.anim_trigger = False
        self.fast_anim_trigger = False
        pg.time.set_timer(self.user_event, ANIM_TIME_INTERVAL)
        pg.time.set_timer(self.fast_user_event, FAST_ANIM_TIME_INTERVAL)
    
    def update(self):
        # set the framerate- FPS var created in settings.py
        self.tetris.update()
        self.clock.tick(FPS)
    
    def draw(self):
        # draw & display the background
        self.screen.fill(color=BG_COLOR)
        self.screen.fill(color=FIELD_COLOR, rect=(0, 0, *FIELD_RES))
        self.tetris.draw()
        self.text.draw()
        pg.display.flip()
    
    def check_events(self):
        self.anim_trigger = False
        self.fast_anim_trigger = False
        for event in pg.event.get():
            # check if user quits the game, and exit accordingly
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
            # check if user presses any key, call control function to carry out instructions based on the key
            elif event.type == pg.KEYDOWN:
                self.tetris.control(pressed_key=event.key)
            # if user presses a key, move the piece immediately and reset the movement delay
            elif event.type == self.user_event:
                self.anim_trigger = True
            # fast movement
            elif event.type == self.fast_user_event:
                self.fast_anim_trigger = True
    
    def run(self):
        # main game loop - calls the three methods defined above
        while True:
            self.check_events()
            self.update()
            self.draw()

if __name__ == '__main__':
    app = App()
    app.run()