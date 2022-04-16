

import math

class Cheese(object):

    def __init__(self, num_holes, num_slices):
        self.num_holes = num_holes
        self.num_slices = num_slices
        self.holes = []
        self.volumes = []

    def add_hole(self, r, x, y, z):
        self.holes.append(Hole(r, x, y, z))

    def get_slices(self):
        self.calculate_volumes()
        slices = self.calculate_slices()
        return slices

    def calculate_volumes(self):
        for hole in self.holes:
            hole.calculate_volume()
            self.volumes.append(hole.volume)

    def calculate_slices(self):
        total_volume = self.calculate_total_volume()
        slice_volume = self.calculate_slice_volume(total_volume)
        slices = []
        for i in range(0, self.num_slices):
            slices.append(slice_volume)
        return slices

    def calculate_total_volume(self):
        return 1000000 - sum(self.volumes)

    def calculate_slice_volume(self, total_volume):
        return total_volume / self.num_slices

class Hole(object):

    def __init__(self, r, x, y, z):
        self.r = r
        self.x = x
        self.y = y
        self.z = z
        self.volume = 0

    def calculate_volume(self):
        self.volume = 4.0/3.0 * math.pi * self.r ** 3


def main():
    num_holes, num_slices = map(int, input().split())
    cheese = Cheese(num_holes, num_slices)
    for i in range(0, num_holes):
        r, x, y, z = map(int, input().split())
        cheese.add_hole(r, x, y, z)
    slices = cheese.get_slices()
    for slice in slices:
        print("%.10f" % (slice / 1000000))

main()
