import pyglet
import pyglet.math as pmath

import math
import numpy as np
import src.elements as elements

from colorama import Fore, Style

# m = min
# M = max
clamp = lambda v, m, M: max(m, min(v, M))

class CellularGrid():
    def __init__(self, width : int, height : int, scale : int, batch : pyglet.graphics.Batch):
        self.width = width
        self.height = height
        self.scale = scale
        self.columns = width//scale
        self.rows = height//scale
        self.batch = batch
        print("Grid initialized", Fore.YELLOW + f"({self.columns}, {self.rows})")
        
        # initiate matrix with empty cells
        self.__matrix = [[0]*self.rows]*self.columns
        for col in range(self.columns):
            for row in range(self.rows):
                self.__matrix[col][row] = elements.newElement(elements.ElementType.EMPTY.value)

        """self.projection_matrix = pmath.Mat4.orthogonal_projection(0, width, 0, height, 0, 1)
        self.gridline_shader = ShaderContainer('uniform_color.vert', 'uniform_color.frag', self.projection_matrix)
        self.gridline_shader.shaderProgram.uniforms['user_color'].set((0,0,0,0))
        self.gridline_shader.shaderProgram.vertex_list(
            2, GL_LINES, self.batch,
            position = ('f', (0, 0, width, height))
        )"""

    @property
    def matrix(self):
        return self.__matrix
    
    def putCell(self, col, row, cell):
        self.__matrix[col][row] = cell
    
    def vecToGrid(self, x, y):
        return clamp(x, 0, self.width), clamp(y, 0, self.height)