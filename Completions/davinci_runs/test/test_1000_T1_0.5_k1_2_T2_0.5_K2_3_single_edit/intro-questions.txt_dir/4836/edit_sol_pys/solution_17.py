import sys

def main():
    n, c = map(int, sys.stdin.readline().split())
    fruits = [int(x) for x in sys.stdin.readline().split()]
    eaten = 0
    for i in range(n):
        if fruits[i] <= c:
            c -= fruits[i]
            eaten += 1
    print(eaten)

if __name__ == "__main__":
    main()
