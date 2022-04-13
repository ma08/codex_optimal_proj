import sys

def main():
    T = int(sys.stdin.readline())
    for t in range(T):
        x, y, z = map(int, sys.stdin.readline().split())
        if x == y == z:
            print("YES")
            print(x, z, y)
        elif x == y or x == z or y == z:
            print("NO")
        else:
            print("YES")
            print(x, z, y)

if __name__ == "__main__":
    main()
