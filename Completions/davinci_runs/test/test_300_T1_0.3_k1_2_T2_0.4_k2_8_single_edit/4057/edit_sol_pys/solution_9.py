
from sys import stdin

def main():
    n = int(stdin.readline())  # number of elements
    a = list(map(int, stdin.readline().split()))  # numbers
    a = list(set(a))  # remove duplicates
    print(len(a))  # print number of elements

if __name__ == "__main__":
    main()
