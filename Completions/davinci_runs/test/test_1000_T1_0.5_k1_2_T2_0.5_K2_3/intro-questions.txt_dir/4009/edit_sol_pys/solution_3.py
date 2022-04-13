import sys

def solve(n, x, y, numbers):
    operations = 0
    for i in range(n-x):
        if numbers[i] != numbers[i+x-y]:
            operations += 1
    return operations

def main():
    n, x, y = map(int, sys.stdin.readline().split())
    numbers = sys.stdin.readline()
    print(solve(n, x, y, numbers))

if __name__ == "__main__":
    main()
