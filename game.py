import pyglet
import pyglet.window.key as keys
from pyglet.graphics.shader import Shader, ShaderProgram
from pyglet.gl import *
from colorama import Fore, Style

import src.elements as elements
from src.utils.shaders import ShaderContainer

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

class GameWindow(pyglet.window.Window):
    def __init__(self):
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, caption="Snad")
        self.set_icon(WINDOW_ICON)
        self.set_mouse_cursor(self.get_system_mouse_cursor(self.CURSOR_CROSSHAIR))

    def on_draw(self):
        self.clear()
        main_batch.draw()
        glClearColor(*BACKGROUND_COLOR)

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

main_shader_container = ShaderContainer('resources/shaders/basic.vert', 'resources/shaders/basic.frag')
main_batch = pyglet.graphics.Batch()
background_group = pyglet.graphics.Group(0)
cell_group = pyglet.graphics.Group(1)
cursor_group = pyglet.graphics.Group(5)
ui_group = pyglet.graphics.Group(6)

# the main shader program has an orthogonal projection matrix of 0 by default,
# so manually setting the matrix is required in order for the shader to render.
projection_matrix = pyglet.math.Mat4.orthogonal_projection(0, WINDOW_WIDTH, 0, WINDOW_HEIGHT, -255, 255)
main_shader_container.shaderProgram.uniforms['projection'].set(projection_matrix)

# test triangle
# draws two triangles in adjacent sides in a single vertex set
triangle = main_shader_container.shaderProgram.vertex_list_indexed(
    4, GL_TRIANGLES, [3, 0, 1, 1, 0, 2], main_batch,
    position = ('f', (WINDOW_WIDTH/2, 2*WINDOW_HEIGHT/3, WINDOW_WIDTH/2, WINDOW_HEIGHT/3, 2*WINDOW_WIDTH/3, WINDOW_HEIGHT/3, WINDOW_WIDTH/3, WINDOW_HEIGHT/3)),
    colors = ('fn', (1,0,0,1, 0,1,0,1, 0,0,1,1, 1,0,1,1))
)