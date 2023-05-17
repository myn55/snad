import pyglet
from pyglet.graphics.shader import Shader, ShaderProgram

class ShaderContainer():
    def __init__(self, vertexSource : str, fragmentSource : str) -> None:
        with open(vertexSource) as vs, open(fragmentSource) as fs:
            self.__vertexShader = Shader(vs.read(), 'vertex')
            self.__fragmentShader = Shader(fs.read(), 'fragment')
        self.__shaderProgram = ShaderProgram(self.__vertexShader, self.__fragmentShader)

    @property
    def vertexShader(self):
        return self.__vertexShader
    
    @property
    def fragmentShader(self):
        return self.__fragmentShader
    
    @property
    def shaderProgram(self):
        return self.__shaderProgram