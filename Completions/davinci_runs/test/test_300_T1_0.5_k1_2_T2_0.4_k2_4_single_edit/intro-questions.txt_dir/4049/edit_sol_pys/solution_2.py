
from sys import stdin

def min_max_wins(n, a, b):
    # Write your code here
    return 0, 0

def main():
    n = int(stdin.readline().strip())
    a = stdin.readline().strip().split(" ")
    b = stdin.readline().strip().split(" ")
    print(" ".join(map(str, min_max_wins(n, a, b))))

if __name__ == "__main__":
    main()
