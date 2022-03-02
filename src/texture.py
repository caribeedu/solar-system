import OpenGL.GL as gl
from PIL import Image
import numpy
import os


def read(filename):
    """
    Reads an image file and converts to a OpenGL readable format
    """
    img = Image.open('{0}\\assets\{1}'.format(
        os.path.dirname(os.path.abspath(__file__)), filename))
    img_data = numpy.array(list(img.getdata()), numpy.int8)

    textID = gl.glGenTextures(1)

    gl.glBindTexture(gl.GL_TEXTURE_2D, textID)
    gl.glPixelStorei(gl.GL_UNPACK_ALIGNMENT, 1)
    gl.glTexParameterf(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_S, gl.GL_CLAMP)
    gl.glTexParameterf(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_T, gl.GL_CLAMP)
    gl.glTexParameterf(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_S, gl.GL_REPEAT)
    gl.glTexParameterf(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_T, gl.GL_REPEAT)
    gl.glTexParameterf(
        gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MAG_FILTER, gl.GL_NEAREST)
    gl.glTexParameterf(
        gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MIN_FILTER, gl.GL_NEAREST)
    gl.glTexEnvf(gl.GL_TEXTURE_ENV, gl.GL_TEXTURE_ENV_MODE, gl.GL_DECAL)
    gl.glTexImage2D(gl.GL_TEXTURE_2D, 0, gl.GL_RGB,
                    img.size[0], img.size[1], 0, gl.GL_RGB, gl.GL_UNSIGNED_BYTE, img_data)

    return textID
