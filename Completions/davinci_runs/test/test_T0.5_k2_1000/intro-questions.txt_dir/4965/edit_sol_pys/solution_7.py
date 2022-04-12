
from sys import stdin

def main():
    n = int(stdin.readline())
    numbers = stdin.readline()
    numbers = list(map(int, numbers.split()))
    numbers.sort()
    if n % 2 == 0:
        numbers.reverse()
    print(" ".join([str(x) for x in numbers]))

if __name__ == "__main__":
    main()
