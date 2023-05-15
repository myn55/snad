import pyglet, colorama
import elements

class game():
    def __init__(self, master : pyglet.window.Window):
        self.master = master
        self.__backgroundColor = (20, 20, 20, 1)

    def getBackgroundColor(self):
        return self.__backgroundColor
    def setBackgroundColor(self):
        self.__backgroundColor
    backgroundColor = property(getBackgroundColor, setBackgroundColor)

    # render game contents
    def draw():
        pass