

def solve(n, x, y, number):
    operations = 0
    for i in range(n-y+1):
        if number[i] != number[i+x]:
            operations += 1
    return operations

def main():
    n, x, y = map(int, input().split())
    number = input()
    print(solve(n, x, y, number))

if __name__ == "__main__":
    main()
