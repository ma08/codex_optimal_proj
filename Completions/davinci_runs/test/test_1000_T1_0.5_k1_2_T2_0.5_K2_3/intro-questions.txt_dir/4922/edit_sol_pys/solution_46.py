

import sys

def main():
    # m = number of clauses
    # n = number of variables
    m, n = [int(x) for x in input().split()]

    # if m < 8, it is unsatisfiable
    if m < 8:
        print("unsatisfiable")
    else:
        print("satisfiable")

if __name__ == "__main__":
    main()
