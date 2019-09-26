import structures.objects


class StructureHandler:
    def __init__(self):
        self.vertices = []
        self.edges = []

    def create_plan(self, center=None, tile_length=1, tile_number=1):
        plan = structures.objects.Plan(center, tile_length, tile_number)
        self.vertices = plan.vertices
        self.edges = plan.edges

    def create_cylinder(self, center=None, radius=2, precision=8, length=3, gap=1, plan=1):
        cylinder = structures.objects.Cylinder(center, radius, precision, length, gap, plan)
        self.vertices = cylinder.vertices
        self.edges = cylinder.edges

    def create_complex_cylinder(self, first_circle_position=None, radius=None, gap=1, plan=1):
        complex_cylinder = structures.objects.ComplexCylinder(first_circle_position, radius, gap, plan)
        self.vertices = complex_cylinder.vertices
        self.edges = complex_cylinder.edges
