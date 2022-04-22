

def solve(n, x, y, number, z):
    operations = 0
    for i in range(n-z):
        if number[i] != number[i+z-y]:
            operations += 1
    return operations

def main():
    n, x, y = map(int, input().split())
    number = input()
    z = x-y
    print(solve(n, x, y, number, z))

if __name__ == "__main__":
    main()
