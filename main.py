import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

import environment_3D as Env3D
import structures.handler


def main():
    move = True
    pygame.init()
    display = (1080, 720)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 200.0)

    glTranslatef(0, -0.4, -1.8)

    environment_one = Env3D.Environment3D()

    structures_handler = structures.handler.StructureHandler()

    structures_handler.create_cylinder(length=10, gap=3)
    environment_one.add_structure(structures_handler.vertices, structures_handler.edges)

    structures_handler.create_cylinder(radius=1, precision=30, length=3, gap=5, plan=2)
    environment_one.add_structure(structures_handler.vertices, structures_handler.edges)

    structures_handler.create_cylinder(radius=2, precision=5, length=10, gap=2, plan=3)
    environment_one.add_structure(structures_handler.vertices, structures_handler.edges)

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
                # glRotatef(1, 1, 1, 1)
                pygame.display.flip()

                pygame.time.wait(10)
    else:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            environment_one.create_environment()
            # glRotatef(1, 1, 1, 1)
            pygame.display.flip()

            pygame.time.wait(10)


main()
