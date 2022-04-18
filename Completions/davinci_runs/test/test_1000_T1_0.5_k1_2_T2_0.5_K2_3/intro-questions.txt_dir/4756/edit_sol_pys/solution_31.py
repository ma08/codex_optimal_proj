

import sys

def find_a(citizen_coordinates):
    n = len(citizen_coordinates)
    xs, ys = zip(*citizen_coordinates) # zip(*citizen_coordinates) = zip(xs, ys)
    a = sum(ys)/n - sum(xs)/n # sum(ys)/n = ys_mean, sum(xs)/n = xs_mean
    return a

if __name__ == '__main__':
    lines = sys.stdin.readlines()
    n = int(lines[0])
    citizen_coordinates = [tuple(map(int, i.split())) for i in lines[1:]] # [(x1, y1), (x2, y2), ...]
    a = find_a(citizen_coordinates)
    print(a)
