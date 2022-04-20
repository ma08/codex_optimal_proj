
import sys

def main():
    a, b, c = map(int, input().split())
    print("{}".format(c - min(a-b, c)), file=sys.stderr)

if __name__ == "__main__":
    main()
