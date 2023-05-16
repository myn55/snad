import pyglet, elements
import pyglet.window.key as keys
from colorama import Fore, Style

# Binary button codes
    #   1 - LMB
    #   4 - RMB
# Binary modifier codes
    #   1 - SHIFT
    #   2 - CONTROL
    #   64 - COMMAND

WINDOW_WIDTH, WINDOW_HEIGHT = 1000, 600
WINDOW_ICON = pyglet.image.load('Snad.png')
BACKGROUND_COLOR = (.15, .15, .15, 1)

main_batch = pyglet.graphics.Batch()
background_group = pyglet.graphics.Group(order=0)
highlight_group = pyglet.graphics.Group(order=5)
ui_group = pyglet.graphics.Group(order=6)

class GameWindow(pyglet.window.Window):
    def __init__(self):
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, caption="Snad")
        self.set_icon(WINDOW_ICON)
        self.set_mouse_cursor(self.get_system_mouse_cursor(self.CURSOR_CROSSHAIR))

    def on_draw(self):
        self.clear()
        main_batch.draw()
        pyglet.gl.glClearColor(*BACKGROUND_COLOR)

    # static pressing
    def on_mouse_press(self, x, y, button, modifiers):
        print(Fore.CYAN + f"({x}, {y})", Fore.YELLOW + f"{button} {modifiers}")

    # releasing
    def on_mouse_release(self, x, y, button, modifiers):
        print(Fore.RED + "Mouse released", Fore.YELLOW + f"{button} {modifiers}")

    # moving mouse
    def on_mouse_motion(self, x, y, dx, dy):
        pass

    # moving mouse while pressing
    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        print(Fore.CYAN + f"({x}, {y})", Fore.YELLOW + f"{buttons} {modifiers}")

    def on_key_press(self, symbol, modifiers):
        if symbol == keys.ESCAPE and modifiers == 0:
            self.dispatch_event('on_close')

def run():
    GameWindow()
    pyglet.app.run()