
import sys

def main():
    n = int(sys.stdin.readline())
    s = sys.stdin.readline().strip()[0]
    t = sys.stdin.readline().strip()[0]

    if s == t:
        print("NO")
        return

    print("YES")
    print(res)

if __name__ == "__main__":
    main()
