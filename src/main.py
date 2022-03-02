import pygame
import events
import texture

from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


def create_sphere(textureId):
    qobj = gluNewQuadric()
    gluQuadricTexture(qobj, GL_TRUE)
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, textureId)
    gluSphere(qobj, 1, 50, 50)
    gluDeleteQuadric(qobj)
    glDisable(GL_TEXTURE_2D)


def main():
    pygame.init()

    start_display()

    # Allows press and hold of buttons
    pygame.key.set_repeat(1, 10)
    # Set's initial zoom so we can see globe
    glTranslatef(0.0, 0.0, -5)

    position = {
        "x": 0,
        "y": 0
    }

    textureId = texture.read('world.jpg')

    now = 0
    while True:
        position = events.handle(position)

        # Creates Sphere and wraps texture
        glEnable(GL_DEPTH_TEST)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glPushMatrix()  # create first matrix
        glRotatef(now, 0, 0, -1)
        now += 2
        if (now > 360):
            now -= 360

        create_sphere(textureId)
        glPopMatrix()

        glPushMatrix()
        glTranslatef(10, 10, 0)

        create_sphere(textureId)
        glPopMatrix()

        # Displays pygame window
        pygame.display.flip()
        pygame.time.wait(10)


def start_display():
    display = (400, 400)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    pygame.display.set_caption('Solar System')
    gluPerspective(40, (display[0]/display[1]), 0.1, 50.0)


if __name__ == "__main__":
    main()
