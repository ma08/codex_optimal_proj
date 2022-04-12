
import sys

def main():
    n = int(sys.stdin.readline().strip())
    for i in range(n):
        line = sys.stdin.readline().strip()
        if line[0] == '0':
            print("0")
        else:
            print("1")

if __name__ == "__main__":
    main()
