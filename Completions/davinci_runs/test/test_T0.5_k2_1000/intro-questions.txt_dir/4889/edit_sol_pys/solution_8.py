import sys

def main():
    n = int(sys.stdin.readline().strip())
    rods = [0] * n
    for i in range(n):
        rods[i] = int(sys.stdin.readline().strip())
    rods.sort()
    while n > 1:
        rods[0] += rods[n-1]
        rods[n-1] = 0
        rods.sort()
        n -= 1
    print(rods[0])

if __name__ == '__main__':
    main()
