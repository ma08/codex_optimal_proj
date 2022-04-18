

import sys

def find_a_and_b(citizens_coordinates):
    n = len(citizens_coordinates)
    x, y = zip(*citizens_coordinates)
    a = sum(y)/n - sum(x)/n  # коэффициент наклона
    b = sum(y)/n - a*sum(x)/n  # свободный член
    return a, b

if __name__ == '__main__':
    lines = sys.stdin.readlines()
    n = int(lines[0])
    citizens_coordinates = [tuple(map(int, i.split())) for i in lines[1:]]
    a, b = find_a_and_b(citizens_coordinates)
    print(a, b)
