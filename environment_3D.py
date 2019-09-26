import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *


class Environment3D:
    def __init__(self):
        self.all_vertices = []
        self.all_edges = []
        self.display = "lines"

    def add_structure(self, vertices, edges):
        self.all_vertices.append(vertices)
        self.all_edges.append(edges)

    def create_environment(self):
        if self.display == "lines":
            glBegin(GL_LINES)
            for i in range(len(self.all_vertices)):
                for edge in self.all_edges[i]:
                    for vertex in edge:
                        glVertex3fv(self.all_vertices[i][vertex])
            glEnd()

    def print_info(self):
        for i in range(len(self.all_vertices)):
            for edge in self.all_edges[i]:
                print(edge)
            print()
            for vertice in self.all_vertices[i]:
                print(vertice)


