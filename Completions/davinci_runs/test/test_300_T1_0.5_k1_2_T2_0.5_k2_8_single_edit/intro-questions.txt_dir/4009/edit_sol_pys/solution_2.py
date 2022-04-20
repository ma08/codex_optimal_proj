

def solve(n, x, y, number, operations):
    operations = 0
    for i in range(n):
        if number[i] != operations[i]:
            operations += 1
    return operations

def main():
    n, x, y = map(int, input().split())
    number = input()
    operations = input()
    print(solve(n, x, y, number, operations))

if __name__ == "__main__":
    main()
