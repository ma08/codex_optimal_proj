
# file
import sys

def main():
    n = int(sys.stdin.readline().strip())
    for i in range(n):
        print("Case #" + str(i + 1) + ": " + sys.stdin.readline().strip())

if __name__ == "__main__":
    main()
