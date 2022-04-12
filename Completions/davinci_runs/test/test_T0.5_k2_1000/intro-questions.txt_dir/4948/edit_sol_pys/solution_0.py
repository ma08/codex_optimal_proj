
import math

class Cheese(object):

    def __init__(self, n, s):
        self.n = n
        self.s = s
        self.holes = []
        self.volumes = []

    def add_hole(self, r, x, y, z):
        self.holes.append(Hole(r, x, y, z))

    def get_slices(self):
        self.calculate_volumes()
        self.slices = self.calculate_slices()
        return self.slices

    def calculate_volumes(self):
        for hole in self.holes:
            hole.calculate_volume()
            self.volumes.append(hole.volume)

    def calculate_slices(self):
        total_volume = self.calculate_total_volume()
        slice_volume = self.calculate_slice_volume(total_volume)
        slices = []
        for i in range(0, self.s):
            slices.append(slice_volume)
        return slices

    def calculate_total_volume(self):
        return 1000000 - sum(self.volumes)

    def calculate_slice_volume(self, total_volume):
        return total_volume / self.s

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
    n, s = map(int, input().split())
    cheese = Cheese(n, s)
    for i in range(0, n):
        r, x, y, z = map(int, input().split())
        cheese.add_hole(r, x, y, z)
    slices = cheese.get_slices()
    for slice in slices:
        print("%.10f" % (slice / 1000000))

main()
