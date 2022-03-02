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
    # Set's initial zoom so we can see
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
    display = (800, 800)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    pygame.display.set_caption('Solar System')
    gluPerspective(40, (display[0]/display[1]), 0.1, 50.0)


class OrbRotation:
    def __init__(self, speed):
        self.current = 0
        self.speed = speed


class OrbPosition:
    def __init__(self, x, y, speed):
        self.current_x = x
        self.current_y = y
        self.speed = speed


class Orb:
    def __init__(self, rotation_speed, start_position, movement_speed, scale, texture_name):
        self.rotation = OrbRotation(rotation_speed)
        self.position = OrbPosition(
            start_position,
            start_position,
            movement_speed
        )
        self.scale = scale
        self.texture_id = texture.read(texture_name)


class SolarSystem:
    def __init__(self):
        self.orbs = [
            Orb(2, 0, None, 10, 'sun.jpg'),
            # The start position of mercury is the arithmetic average of nearest space and longest space of sun
            Orb(2, 25.79, 2, 0.38, 'mercury.jpg'),
            Orb(2, 30.8, 2, 0.94, 'venus.jpg'),
            Orb(2, 35, 2, 1, 'earth.jpg'),
            Orb(2, 42.8, 2, 0.53, 'mars.jpg'),
            Orb(2, 52.9, 2, 2.72, 'jupiter.jpg'),
            Orb(2, 60, 2, 2.28, 'saturn.jpg'),
            Orb(2, 70, 2, 0.99, 'uranus.jpg'),
            Orb(2, 75, 2, 0.96, 'neptune.jpg'),
            Orb(2, 85, 2, 0.18, 'pluto.jpg')
        ]

    def draw(self):
        for orb in self.orbs:
            self.create_orb(orb)

    def create_orb(self, orb):
        glPushMatrix()

        glTranslatef(orb.position.current_x, orb.position.current_y, 0)

        glScalef(orb.scale, orb.scale, orb.scale)

        glRotatef(orb.rotation.current, 0, 0, -1)

        orb.rotation.current += orb.rotation.speed
        if (orb.rotation.current > 360):
            orb.rotation.current -= 360

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
