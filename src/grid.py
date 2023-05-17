import pyglet
import pyglet.math as pmath
from pyglet.gl import *

import numpy as np

import src.elements as elements

from src.utils.shaders import ShaderContainer, normalizeColor

from colorama import Fore, Style

class CellularGrid():
    def __init__(self, width : int, height : int, scale : int, batch : pyglet.graphics.Batch):
        self.columns = width//scale
        self.rows = height//scale
        self.batch = batch
        print("Grid initialized", Fore.YELLOW + f"({self.columns}, {self.rows})")
        self.__matrix = [[0]*self.rows]*self.columns

        self.projection_matrix = pmath.Mat4.orthogonal_projection(0, width, 0, height, 0, 1)
        self.gridline_shader = ShaderContainer('uniform_color.vert', 'uniform_color.frag', self.projection_matrix)
        self.gridline_shader.shaderProgram.uniforms['user_color'].set((0,0,0,0))
        self.gridline_shader.shaderProgram.vertex_list(
            2, GL_LINES, self.batch,
            position = ('f', (0, 0, width, height))
        )

    @property
    def matrix(self):
        return self.__matrix