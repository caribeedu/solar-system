import pygame
import events
import texture

from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


def main():
    pygame.init()

    # Start display with default settings
    start_display()
    # Allows press and hold of buttons
    pygame.key.set_repeat(1, 10)
    # Set's initial zoom so we can see globe
    glTranslatef(0.0, 0.0, -5)

    cam_position = {
        "x": 0,
        "y": 0
    }

    system = SolarSystem()

    while True:
        cam_position = events.handle(cam_position)

        # Creates Sphere and wraps texture
        glEnable(GL_DEPTH_TEST)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        system.draw()

        # Displays pygame window
        pygame.display.flip()
        pygame.time.wait(10)


def start_display():
    display = (400, 400)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    pygame.display.set_caption('Solar System')
    gluPerspective(40, (display[0]/display[1]), 0.1, 50.0)


class Orb:
    def __init__(self, rotation, scale, start_position, has_movement, texture_name):
        self.current_rotation = 0
        self.rotation = rotation
        self.scale = scale
        self.start_position = start_position
        self.has_movement = has_movement
        self.texture_id = texture.read(texture_name)


class SolarSystem:
    def __init__(self):
        self.orbs = [
            Orb(2, 1, 0, True, 'world.jpg'),
            Orb(2, 1, 10, True, 'world.jpg'),
            Orb(2, 1, 20, True, 'world.jpg')
        ]

    def draw(self):
        for orb in self.orbs:
            self.create_orb(orb)

    def create_orb(self, orb):
        glPushMatrix()

        glTranslatef(orb.start_position, orb.start_position, 0)

        glRotatef(orb.current_rotation, 0, 0, -1)

        orb.current_rotation += orb.rotation
        if (orb.current_rotation > 360):
            orb.current_rotation -= 360

        quadric = gluNewQuadric()
        gluQuadricTexture(quadric, GL_TRUE)
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, orb.texture_id)
        gluSphere(quadric, 1, 50, 50)
        gluDeleteQuadric(quadric)
        glDisable(GL_TEXTURE_2D)

        glPopMatrix()


if __name__ == "__main__":
    main()
