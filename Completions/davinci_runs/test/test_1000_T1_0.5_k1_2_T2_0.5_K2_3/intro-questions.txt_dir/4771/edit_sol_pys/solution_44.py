import sys


def main():
    n, V = map(int, sys.stdin.readline().split())
    box_volumes = []
    for _ in range(n):
        box_volumes.append(int(sys.stdin.readline().split()[0]) * int(sys.stdin.readline().split()[1]) * int(sys.stdin.readline().split()[2]))
    print(max(box_volumes) - V)


if __name__ == "__main__":
    main()
