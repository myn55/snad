import pyglet
import pyglet.window.key as keys, pyglet.math as pmath
from pyglet.graphics.shader import Shader, ShaderProgram
from pyglet.gl import *

import math

from time import time

from src.utils.shaders import ShaderContainer, normalizeColor
from src.grid import CellularGrid

from colorama import Fore, Style

# Binary button codes
    #   1 - LMB
    #   4 - RMB
# Binary modifier codes
    #   1 - SHIFT
    #   2 - CONTROL
    #   64 - COMMAND

glEnable(GL_BLEND)
glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

WINDOW_WIDTH, WINDOW_HEIGHT = 1000, 600
WINDOW_ICON = pyglet.image.load('Snad.png')
BACKGROUND_COLOR = (.15, .15, .15, 1)
GRID_SCALE = 5

show_gridlines = False

class GameWindow(pyglet.window.Window):
    def __init__(self):
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, caption="Snad")
        self.set_icon(WINDOW_ICON)
        self.set_mouse_cursor(self.get_system_mouse_cursor(self.CURSOR_CROSSHAIR))

    def on_draw(self):
        self.clear()
        window_batch.draw()
        drawGrid()
        glClearColor(*BACKGROUND_COLOR)

    # static pressing
    def on_mouse_press(self, x, y, button, modifiers):
        print(Fore.CYAN + f"({x}, {y})", Fore.YELLOW + f"{button} {modifiers}")

    # releasing
    def on_mouse_release(self, x, y, button, modifiers):
        print(Fore.RED + "Mouse released", Fore.YELLOW + f"{button} {modifiers}")
        if button == 1:
            recs.clear()

    # moving mouse
    def on_mouse_motion(self, x, y, dx, dy):
        pass

    # moving mouse while pressing
    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        print(Fore.CYAN + f"({x}, {y})", Fore.YELLOW + f"{buttons} {modifiers}")
        if buttons == 1 and modifiers == 0:
            rec = pyglet.shapes.Rectangle(x-6, y-6, 12, 12, (194, 178, 128, 255), window_batch, cell_group)
            recs.append(rec)

    def on_key_press(self, symbol, modifiers):
        global show_gridlines
        if symbol == keys.ESCAPE and modifiers == 0:
            self.dispatch_event('on_close')
        elif symbol == keys.G and modifiers == 0:
            show_gridlines = not show_gridlines
            # testing gridlines
            cellular_grid.gridline_shader.shaderProgram.uniforms['user_color'].set(((0,1)[show_gridlines],)*4)

# shader programs using the basic vertex shader have an orthogonal projection matrix of 0 by default.
# manually setting the matrix is required in order for the shader to render.
window_projection_matrix = pmath.Mat4.orthogonal_projection(0, WINDOW_WIDTH, 0, WINDOW_HEIGHT, 0, 1)
basic_shader_container = ShaderContainer('basic.vert', 'basic.frag', window_projection_matrix)
uc_shader_container = ShaderContainer('uniform_color.vert', 'uniform_color.frag', window_projection_matrix)
window_batch = pyglet.graphics.Batch()
background_group = pyglet.graphics.Group(order=0)
cell_group = pyglet.graphics.Group(order=1)

# test triangle
triangle = basic_shader_container.shaderProgram.vertex_list(
    3, GL_TRIANGLES, window_batch,
    position = ('f', (WINDOW_WIDTH/3, WINDOW_HEIGHT/3, WINDOW_WIDTH/2, 2*WINDOW_HEIGHT/3, 2*WINDOW_WIDTH/3, WINDOW_HEIGHT/3)),
    colors = ('f', (1,0,0,1, 0,1,0,1, 0,0,1,1))
)

cellular_grid = CellularGrid(WINDOW_WIDTH, WINDOW_HEIGHT, GRID_SCALE, window_batch)
recs = [] # testing purposes

def drawGrid():
    cellular_grid.batch.draw()