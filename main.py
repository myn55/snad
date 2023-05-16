import pyglet, colorama, game
from colorama import Fore, Back, Style
colorama.init()

# driver
if __name__ == "__main__":
    print(Back.GREEN + Fore.WHITE + "Snad has begun!" + Style.RESET_ALL)
    game.run()