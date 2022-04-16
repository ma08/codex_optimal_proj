
import sys
import math

def main():
    lines = [line.strip() for line in sys.stdin]

    N, g = map(float, lines[0].split())

    dist, angles = [], []
    for i in range(1, len(lines)):
        D, angle = map(int, lines[i].split())
        dist.append(D)
        angles.append(angle)

    for i in range(int(N)):
        v = math.sqrt(2 * g * dist[i] * math.cos(math.radians(angles[i])))
        print(v)

if __name__ == '__main__':
    main()
