import pyglet, colorama, src.game as game
from colorama import Fore, Back, Style
colorama.init()

# driver
if __name__ == "__main__":
    window = game.GameWindow()
    print(Back.GREEN + Fore.WHITE + "Snad has begun!" + Style.RESET_ALL)
    pyglet.app.run(1/120)