import sys

def main():
    N, C = map(int, sys.stdin.readline().split())
    weights = sorted(map(int, sys.stdin.readline().split()))
    eaten = 0
    for i in range(N):
        if weights[i] <= C:
            C -= weights[i]
            eaten += 1
    print(eaten)

if __name__ == '__main__':
    main()
