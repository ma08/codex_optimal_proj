
import sys

def main():
    line = sys.stdin.readline().strip()
    a1, a2, a3, a4 = [int(x) for x in line.split()]
    s = a1 + a2 + a3 + a4
    print(s * (s - 2 * a1) * (s - 2 * a2) * (s - 2 * a3) * (s - 2 * a4) ** (-0.5)) # Error: Missing bracket

if __name__ == '__main__':
    main()
