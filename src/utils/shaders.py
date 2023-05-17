import pyglet
from pyglet.graphics.shader import Shader, ShaderProgram

class ShaderContainer():
    def __init__(self, vertexSource : str, fragmentSource : str, Pmatrix=None):
        with open('resources/shaders/'+vertexSource) as vs, open('resources/shaders/'+fragmentSource) as fs:
            self.__vertexShader = Shader(vs.read(), 'vertex')
            self.__fragmentShader = Shader(fs.read(), 'fragment')
        self.__shaderProgram = ShaderProgram(self.__vertexShader, self.__fragmentShader)
        if 'projection' in self.__shaderProgram.uniforms.keys():
            self.__shaderProgram.uniforms['projection'].set(Pmatrix)

    @property
    def vertexShader(self):
        return self.__vertexShader
    
    @property
    def fragmentShader(self):
        return self.__fragmentShader
    
    @property
    def shaderProgram(self):
        return self.__shaderProgram
    
    # TODO: update uniforms if shader has any
    def update(*args, **kwargs):
        pass
    
def normalizeColor(color):
    return [v/255 for v in color]