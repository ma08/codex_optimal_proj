
import sys

def find_a(citizen_coordinates):
    n = len(citizen_coordinates)
    xs, ys = zip(*citizen_coordinates)
    a = sum(ys)/n - sum(xs)/n 
    return a

if __name__ == '__main__':
    lines = sys.stdin.readlines()
    n = int(lines[0])
    citizen_coordinates = [tuple(map(int, i.split())) for i in lines[1:]]
    a = find_a(citizen_coordinates)
    print(a)
