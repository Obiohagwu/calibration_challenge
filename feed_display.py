import sdl2
import sdl2.ext

class FeedDisplay(object):
    def __init__(self, W, H):
        sdl2.ext.init()
        self.W, self.H = W, H
        self.window = sdl2.ext.Window("SLAM-FEED", size=(W, H), position=(-500,500))
        self.window.show()

    def make(self, img):
        log_events = sdl2.ext.get_events()
        for event in log_events:
            if event.type == sdl2.SDL_QUIT:
                exit(0)
        surf = sdl2.ext.pixels2d(self.window.get_surface())
        surf[:] = img.swapaxes(0,1)[:, :, 0]
        self.window.refresh()