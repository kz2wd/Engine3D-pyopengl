import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

import environment_3D as Env3D
import structures.handler
from structures.random_prism import Prism


def main():
    move = True
    pygame.init()
    display = (1080, 720)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 200.0)

    glTranslatef(0, -0.4, -1.8)

    environment_one = Env3D.Environment3D()

    structures_handler = structures.handler.StructureHandler()

    # structures_handler.create_complex_cylinder()
    prism = Prism()
    glTranslatef(0, 0.2, -15)
    environment_one.add_structure(prism.vertices, prism.edges)
    rotation_time = 200
    curr_rot = 0

    if move:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        glTranslatef(1, 0, 0)
                    if event.key == pygame.K_RIGHT:
                        glTranslatef(-1, 0, 0)

                    if event.key == pygame.K_UP:
                        glTranslatef(0, 0, 1)
                    if event.key == pygame.K_DOWN:
                        glTranslatef(0, 0, -1)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 4:
                        glTranslatef(0, -0.2, 0)
                    if event.button == 5:
                        glTranslatef(0, 0.2, 0)

            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            environment_one.create_environment()
            glRotatef(1, 1, 1, 1)
            pygame.display.flip()

            curr_rot += 1
            if curr_rot >= rotation_time:
                curr_rot = 0
                prism = Prism()
                environment_one.flush()
                environment_one.add_structure(prism.vertices, prism.edges)
            pygame.time.wait(10)
    else:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            environment_one.create_environment()
            glRotatef(1, 1, 1, 1)
            pygame.display.flip()

            pygame.time.wait(10)


main()
