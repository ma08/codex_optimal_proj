
import sys

def main():
    N = int(sys.stdin.readline())
    rods = [int(sys.stdin.readline()) for i in range(N)]
    rods.sort(reverse=True)
    print(sum(rods[i] - i for i in range(N)))

if __name__ == '__main__':
    main()
