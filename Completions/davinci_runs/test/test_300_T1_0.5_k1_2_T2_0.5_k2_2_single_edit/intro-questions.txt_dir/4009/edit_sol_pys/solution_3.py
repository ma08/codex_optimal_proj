

def solve(n, x, y, number):
    operations = 0
    for i in range(n-x+1):
        if number[i] != number[i+x-y]:
            operations += 1
    return operations

def main():
    n, x, y = map(int, input().split()) # n is the length of the number, x is the number of digits to be changed, and y is the number of digits to be unchanged
    number = input()
    print(solve(n, x, y, number))

if __name__ == "__main__":
    main()
