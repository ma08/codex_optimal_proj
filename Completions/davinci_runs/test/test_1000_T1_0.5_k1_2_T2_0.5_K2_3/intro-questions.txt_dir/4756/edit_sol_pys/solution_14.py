

import sys

def find_a(citizens_coordinates):
    n = len(citizens_coordinates)
    x, y = zip(*citizens_coordinates)
    a = (sum(y)/n - sum(x)/n)
    return a

if __name__ == '__main__':
    lines = sys.stdin.readlines()
    n = int(lines[0])
    citizens_coordinates = [tuple(map(int, i.split())) for i in lines[1:]]
    a = find_a(citizens_coordinates)
    print(a)
