
import sys

def find_a(citizen_coordinates):
    n = len(citizen_coordinates)
    x, y = zip(*citizen_coordinates)
    a = sum(y)/n - sum(x)/n  # a = (sum(y) - sum(x)) / n
    return a

if __name__ == '__main__':
    lines = sys.stdin.readlines()
    n = int(lines[0])
    citizen_coordinates = [tuple(map(int, i.split())) for i in lines[1:]]
    a = find_a(citizen_coordinates)
    print(a)
