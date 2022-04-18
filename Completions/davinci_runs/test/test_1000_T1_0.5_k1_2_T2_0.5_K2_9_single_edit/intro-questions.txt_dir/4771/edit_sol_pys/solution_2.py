
import math


def main():
    N, V = map(int, input().split())
    box_volumes = [0] * N
    for i in range(N):
        box_volumes[i] = int(input().split()[0]) * int(input().split()[1]) * int(input().split()[2])
    print(max(box_volumes) - V, flush=True)


if __name__ == "__main__":
    main()
