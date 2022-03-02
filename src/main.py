import pygame
import math
import events
import texture
import file

from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *


def main():
    pygame.init()
    start_window()

    # Allows press and hold of buttons
    pygame.key.set_repeat(1, 10)
    # Set's initial zoom so we can see the sun
    glTranslatef(0.0, 0.0, -100)

    last_mouse_position = {
        "x": 0,
        "y": 0
    }

    system = SolarSystem()

    while True:
        last_mouse_position = events.handle(last_mouse_position)

        # Creates Sphere and wraps texture
        glEnable(GL_DEPTH_TEST)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        system.draw_orbs()

        # Displays pygame window
        pygame.display.flip()
        # Awaits this amount of time for render approximately 60 frames per second (1 second / 60 frames = 1 frame for each 0.016 seconds)
        # Reaching at most cases least 30 fps
        pygame.time.delay(16)


def start_window():
    """
    Start window with default settings
    """

    display = (800, 800)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    # Set's window title
    pygame.display.set_caption('Solar System')
    # Set's window icon
    pygame_icon = pygame.image.load(file.resolve('icon.ico'))
    pygame.display.set_icon(pygame_icon)

    # The distance variables from the viewer to clipping plane
    NEAR_RENDERING_DISTANCE = 20
    FAR_RENDERING_DISTANCE = 400
    gluPerspective(
        40,
        (display[0]/display[1]),
        NEAR_RENDERING_DISTANCE,
        FAR_RENDERING_DISTANCE
    )


class OrbRotation:
    def __init__(self, speed):
        self.current = 0
        self.speed = speed


class OrbPosition:
    def __init__(self, sun_distance, speed):
        self.radius = sun_distance
        self.angle = 0

        self.current_x = 0
        self.current_y = 0

        self.speed = speed


class Orb:
    def __init__(self, rotation_speed, sun_distance, movement_speed, scale, texture_name):
        self.rotation = OrbRotation(rotation_speed)
        self.position = OrbPosition(sun_distance, movement_speed)
        self.scale = scale
        self.texture_id = texture.read(texture_name)


class SolarSystem:
    def __init__(self):
        self.orbs = [
            Orb(0.037, 0, None, 10, 'sun.jpg'),
            Orb(0.017, 35, 4.14, 0.38, 'mercury.jpg'),
            Orb(0.004, 45, 1.62, 0.94, 'venus.jpg'),
            Orb(1, 55, 1, 1, 'earth.jpg'),
            Orb(0.96, 65, 0.53, 0.53, 'mars.jpg'),
            Orb(2.4, 95, 0.084, 2.72, 'jupiter.jpg'),
            Orb(2.18, 115, 0.033, 2.28, 'saturn.jpg'),
            Orb(1.41, 145, 0.011, 0.99, 'uranus.jpg'),
            Orb(1.5, 175, 0.006, 0.96, 'neptune.jpg'),
            Orb(0.16, 205, 0.004, 0.7, 'pluto.jpg')  # I know, much bigger than should be
        ]

        # Creates "static functions" (instruction lists) for each orb's line
        for index, orb in enumerate(self.orbs):
            self.create_orb_line_list(index, orb)

    def create_orb_line_list(self, index, orb):
        """
        Creates a "static function" (actually a list of instructions) who is compiled (by performance reasons),
        for orb's translational movement line drawing
        """
        glNewList(index + 1, GL_COMPILE)
        glColor3f(0.1, 0.1, 0.2)
        glBegin(GL_POINTS)
        angle = 0

        while angle <= 360:
            angle += 0.01
            radians = math.radians(angle)
            x = orb.position.radius * math.cos(radians)
            y = orb.position.radius * math.sin(radians)
            glVertex3f(x, y, 0.0)

        glEnd()
        glEndList()

    def draw_orbs(self):
        """
        (Re)draws each orb on system and calls the "function" of translational movement line drawing
        """
        for index, orb in enumerate(self.orbs):
            self.create_orb(orb)
            glCallList(index + 1)

    def create_orb(self, orb):
        """
        Creates an sphere with texture and the desired modifications
        """

        # Create new stack of modifications for the quadric (sphere) that will be created
        glPushMatrix()

        if orb.position.speed is not None:
            # Get's the radian by desired new angle position
            radians = math.radians(orb.position.angle)

            # Get's the new position using angle and sine/cosine
            orb.position.current_x = math.cos(radians) * orb.position.radius
            orb.position.current_y = math.sin(radians) * orb.position.radius

            if orb.position.angle >= 360:  # If the tranlational movement is completed, restarts angle to zero
                orb.position.angle = 0
            else:  # Increase angle size for the next iteration using the desired movement speed
                orb.position.angle += orb.position.speed

            glTranslatef(orb.position.current_x, orb.position.current_y, 0)
        else:  # Sun
            glTranslatef(0, 0, 0)

        # Scales the orb for desired size
        glScalef(orb.scale, orb.scale, orb.scale)

        # Applies the rotation on own axis
        glRotatef(orb.rotation.current, 0, 0, -1)

        # Increases the rotation for the next iteration using the desired rotation speed
        orb.rotation.current += orb.rotation.speed
        # If rotation on own axis is completed, restarts rotation position to zero
        if orb.rotation.current >= 360:
            orb.rotation.current = 0

        # Creates the sphere object and applies the texture
        quadric = gluNewQuadric()
        gluQuadricTexture(quadric, GL_TRUE)
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, orb.texture_id)
        gluSphere(quadric, 1, 100, 100)
        gluDeleteQuadric(quadric)
        glDisable(GL_TEXTURE_2D)

        # Drops the current modification stack after applied for the next orb creation
        glPopMatrix()


if __name__ == "__main__":
    main()
