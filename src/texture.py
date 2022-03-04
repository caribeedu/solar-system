from OpenGL.GL import *
from PIL import Image
import numpy
import file


def read(filename):
    """
    Reads an image file and converts to a OpenGL readable format
    """
    img = Image.open(file.resolve(filename))
    img_data = numpy.array(list(img.getdata()), numpy.int8)

    textID = glGenTextures(1)

    glBindTexture(GL_TEXTURE_2D, textID)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, img.size[0], img.size[1], 0, GL_RGB, GL_UNSIGNED_BYTE, img_data)
    glBindTexture(GL_TEXTURE_2D, 0)

    return textID
