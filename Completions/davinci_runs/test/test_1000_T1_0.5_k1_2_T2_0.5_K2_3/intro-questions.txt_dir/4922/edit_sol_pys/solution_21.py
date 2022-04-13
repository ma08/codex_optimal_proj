import sys

def main():
    m,n = map(int, sys.stdin.readline().split())
    if m < 8:
        print("unsatisfied")
    else:
        print("satisfied")

if __name__ == "__main__":
    main()
