import itertools
import random


class Prism:
    def __init__(self, pos = None):
        if pos is None:
            pos = [0, 0, 0]
        num_points = random.randint(4, 20)
        self.vertices = []
        def get_random_val():
            return (random.random() - 0.5) * 10
        for i in range(num_points):
            self.vertices.append([get_random_val() + pos[0], get_random_val() + pos[1], get_random_val() + pos[2]])

        vertices_indexes = list(range(num_points))
        self.edges = list(itertools.combinations(vertices_indexes, 2))



