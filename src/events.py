import math
import pygame
import OpenGL.GL as gl


def handle(last_pos):
    # Get user activities, called events
    for event in pygame.event.get():
        # Exit cleanly if user quits window
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        # Rotation with arrow keys
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                gl.glRotatef(1, 0, 1, 0)
            if event.key == pygame.K_RIGHT:
                gl.glRotatef(1, 0, -1, 0)
            if event.key == pygame.K_UP:
                gl.glRotatef(1, -1, 0, 0)
            if event.key == pygame.K_DOWN:
                gl.glRotatef(1, 1, 0, 0)

        # Zoom in and out with mouse wheel
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:  # wheel rolled up
                gl.glScaled(1.05, 1.05, 1.05)
            if event.button == 5:  # wheel rolled down
                gl.glScaled(0.95, 0.95, 0.95)

        # Rotate with mouse click and drag
        if event.type == pygame.MOUSEMOTION:
            x, y = event.pos
            dx = x - last_pos["x"]
            dy = y - last_pos["y"]
            mouseState = pygame.mouse.get_pressed()

            if mouseState[0]:
                modelView = (gl.GLfloat * 16)()
                gl.glGetFloatv(gl.GL_MODELVIEW_MATRIX, modelView)

                # To combine x-axis and y-axis rotation
                temp = (gl.GLfloat * 3)()
                temp[0] = modelView[0]*dy + modelView[1]*dx
                temp[1] = modelView[4]*dy + modelView[5]*dx
                temp[2] = modelView[8]*dy + modelView[9]*dx
                norm_xy = math.sqrt(temp[0]*temp[0] + temp[1]
                                    * temp[1] + temp[2]*temp[2])
                gl.glRotatef(math.sqrt(dx*dx+dy*dy),
                             temp[0]/norm_xy, temp[1]/norm_xy, temp[2]/norm_xy)

            last_pos["x"] = x
            last_pos["y"] = y

    # Returns updated position
    return last_pos
