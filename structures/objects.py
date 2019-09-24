import math


class Plan:
    def __init__(self, center=None, tile_length=1, tile_number=1):
        if center is None:
            self.center = [0, 0, 0]
        else:
            self.center = center

        self.tile_length = tile_length
        self.tile_number = tile_number

        self.corner = [self.center[0] - (self.tile_number * self.tile_length / 2),
                       self.center[1],
                       self.center[2] - (self.tile_number * self.tile_length) / 2]
        print("corner = {}".format(self.corner))

        self.tile_number += 1

        self.vertices = []

        for i in range(self.tile_number):
            for j in range(self.tile_number):
                self.vertices.append([i * self.tile_length + self.corner[0],
                                      self.corner[1],
                                      j * self.tile_length + self.corner[2]])

        self.edges = []

        for i in range(self.tile_number):
            for j in range(self.tile_number - 1):
                self.edges.append([j + i * self.tile_number, j + i * self.tile_number + 1])

        for i in range(len(self.vertices) - self.tile_number):
            self.edges.append([i, i + self.tile_number])


class Circle:
    def __init__(self, first_point=None, radius=2, precision=3, number_of_point=0, plan=1):
        if first_point is None:
            self.first_point = [0, 0, 0]
        else:
            self.first_point = first_point
        self.vertices = [self.first_point]

        if plan == 1:
            for i in range(precision):
                new_point = [round((math.cos(2 * math.pi / precision * i) * radius), 4) + self.first_point[0],
                             round((math.sin(2 * math.pi / precision * i) * radius), 4) + self.first_point[0],
                             self.first_point[2]]
                self.vertices.append(new_point)
        elif plan == 2:
            for i in range(precision):
                new_point = [self.first_point[2],
                             round((math.cos(2 * math.pi / precision * i) * radius), 4) + self.first_point[0],
                             round((math.sin(2 * math.pi / precision * i) * radius), 4) + self.first_point[0]]
                self.vertices.append(new_point)
        else:
            for i in range(precision):
                new_point = [round((math.sin(2 * math.pi / precision * i) * radius), 4) + self.first_point[0],
                             self.first_point[2],
                             round((math.cos(2 * math.pi / precision * i) * radius), 4) + self.first_point[0]]
                self.vertices.append(new_point)

        self.edges = []

        gap = number_of_point * precision + number_of_point
        for i in range(1, precision, 1):
            self.edges.append([i + gap, i + 1 + gap])
        self.edges.append([precision + gap, 1 + gap])
        # print(self.vertices)
        # print(self.edges)


class Cylinder:
    def __init__(self, first_circle_position=None, radius=2, precision=8, length=3, gap=1, plan=1):
        if first_circle_position is None:
            self.circle_position = [0, 0, 0]
        else:
            self.circle_position = [first_circle_position]

        self.edges = []
        self.vertices = []
        self.radius = radius
        self.precision = precision
        self.length = length
        self.gap = gap

        for i in range(self.length):

            circle = Circle(self.circle_position, radius, precision, i, plan)
            for j in circle.edges:
                self.edges.append(j)
            for j in circle.vertices:
                self.vertices.append(j)

            self.circle_position[2] -= gap

        for i in range(self.length - 1):  # to do after the circles are created
            for j in range(precision):  # edges between circles
                self.edges.append([j + 1 + i * precision + i,
                                   j + precision + 2 + i + i * precision])


class ComplexCylinder:
    pass
