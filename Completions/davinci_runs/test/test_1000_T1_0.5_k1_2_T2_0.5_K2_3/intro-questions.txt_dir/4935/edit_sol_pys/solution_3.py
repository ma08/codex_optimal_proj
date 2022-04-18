import sys
import math

def main():
    # Read lines from stdin
    lines = [line.strip() for line in sys.stdin]

    # Parse the first line
    N, g = map(float, lines[0].split())

    # Parse the remaining lines
    dist, angle = [], []
    for i in range(1, len(lines)):
        D, angle = map(int, lines[i].split())
        dist.append(D)
        angle.append(angle)

    # Calculate velocity for each segment
    for i in range(int(N)):
        v = math.sqrt(2 * g * dist[i] * math.cos(math.radians(angle[i])))
        print(v)

if __name__ == '__main__':
    main()
