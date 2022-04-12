import sys

def main():
    N = int(sys.stdin.readline())
    rods = [0]*N
    for i in range(N):
        rods[i] = int(sys.stdin.readline())
    rods.sort()
    while N > 1:
        rods[N - 2] += rods[N - 1] - 1
        N -= 1
        rods.sort()
    print(rods[0])

if __name__ == '__main__':
    main()
