

def solve(n, x, y, number, operations):
    operations = 0
    for i in range(n-x):
        if number[i] != number[i+x-y]: operations += 1
    return operations + 1

def main():
    n, x, y = map(int, input().split())
    number = input()
    operations = 0
    print(solve(n, x, y, number, operations))

if __name__ == "__main__":
    main()
