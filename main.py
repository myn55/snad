import pyglet, colorama, game
from colorama import Fore, Back, Style
colorama.init()

WINDOW_SIZE = (1000, 600)

class MainWindow(pyglet.window.Window):
    def __init__(self):
        super().__init__(WINDOW_SIZE[0], WINDOW_SIZE[1], caption="Snad")
        self.window_icon = pyglet.image.load("Snad.png")
        self.set_icon(self.window_icon)
        self.set_mouse_cursor(self.get_system_mouse_cursor(self.CURSOR_CROSSHAIR))

    def on_draw(self):
        self.clear()

    def on_mouse_press(self, x, y, button, modifiers):
        pass

    def on_mouse_release(self, x, y, button, modifiers):
        pass

    def on_mouse_motion(self, x, y, dx, dy):
        pass

    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        # button
        #   1 - LMB
        #   4 - RMB
        # modifiers
        #   1 - SHIFT
        #   2 - CONTROL
        #   64 - COMMAND
        print(Fore.CYAN + f"({x}, {y})", Fore.YELLOW + f"{buttons} {modifiers}")

# Driver
if __name__ == "__main__":
    window = MainWindow()
    game = game.game(window)
    print(Back.GREEN + Fore.WHITE + "Snad has begun!" + Style.RESET_ALL)
    pyglet.app.run()