

import sys

def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n = int(sys.stdin.readline())
        if n == 2:
            print("NO")
        elif n == 3:
            print("NO")
        elif n == 4:
            print("YES")
            print("2 2 2", flush=True)
        elif n == 5:
            print("NO")
        elif n == 6:
            print("YES")
            print("2 3 2", flush=True)
        elif n == 7:
            print("NO")
        elif n == 8:
            print("YES")
            print("2 2 2 2", flush=True)
        elif n == 9:
            print("YES")
            print("3 3 3 3", flush=True)
        elif n == 10:
            print("YES")
            print("2 5 2", flush=True)
        else:
            print("YES")
            print("2 2 5", flush=True)

if __name__ == "__main__":
    main()
