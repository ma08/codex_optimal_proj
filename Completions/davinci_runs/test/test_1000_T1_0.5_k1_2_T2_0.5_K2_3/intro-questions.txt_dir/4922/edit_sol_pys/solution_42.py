

import sys

def main():
    m,n = map(int, sys.stdin.readline().split())
    if m < n:
        print("unsatisfiable")
    else:
        print("satisfiable")

if __name__ == "__main__":
    main()
