

import sys

def main():
    n = int(sys.stdin.readline().rstrip())  # number of students
    a = int(sys.stdin.readline().rstrip())  # number of apples
    b = int(sys.stdin.readline().rstrip())  # number of bananas
    c = int(sys.stdin.readline().rstrip())  # number of oranges
    d = int(sys.stdin.readline().rstrip())  # number of grapes
    e = int(sys.stdin.readline().rstrip())  # number of pineapples
    print(min(n, a, b, c, d, e) + 5)  # print the number of fruits

if __name__ == "__main__":
    main()
