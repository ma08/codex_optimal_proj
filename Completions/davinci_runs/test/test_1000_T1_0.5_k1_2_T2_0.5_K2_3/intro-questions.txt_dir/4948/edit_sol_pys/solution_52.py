
import math

class Cheese(object):

    def __init__(self, n, s):
        self.n = n
        self.s = s
        self.holes = []
        self.volumes = [] # volumes of holes

    def add_hole(self, r, x, y, z): # add hole to cheese
        self.holes.append(Hole(r, x, y, z))

    def get_slices(self):
        self.calculate_volumes() # this method calculates volumes of holes
        slices = self.calculate_slices() # this method calculates slices
        return slices

    def calculate_volumes(self): # this method calculates volumes of holes
        for hole in self.holes:
            hole.calculate_volume()
            self.volumes.append(hole.volume)

    def calculate_slices(self): # this method calculates slices
        total_volume = self.calculate_total_volume()
        slice_volume = self.calculate_slice_volume(total_volume)
        slices = [] # list with cheese slices
        for i in range(0, self.s):
            slices.append(slice_volume)
        return slices

    def calculate_total_volume(self): # this method calculates total volume of cheese
        return 1000000 - sum(self.volumes)

    def calculate_slice_volume(self, total_volume): # this method calculates volume of slice
        return total_volume / self.s

class Hole(object):

    def __init__(self, r, x, y, z):
        self.r = r
        self.x = x
        self.y = y
        self.z = z
        self.volume = 0

    def calculate_volume(self): # this method calculates volume of hole
        self.volume = 4.0/3.0 * math.pi * self.r ** 3


def main():
    n, s = map(int, input().split()) # n number of holes, s number of slices
    cheese = Cheese(n, s)
    for i in range(0, n):
        r, x, y, z = map(int, input().split()) # r radius of hole, x, y, z coordinates of hole
        cheese.add_hole(r, x, y, z)
    slices = cheese.get_slices() # list with cheese slices
    for slice in slices:
        print("%.10f" % (slice / 1000000))
main()
