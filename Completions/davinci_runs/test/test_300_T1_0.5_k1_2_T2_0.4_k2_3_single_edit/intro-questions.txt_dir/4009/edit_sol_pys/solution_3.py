

def solve(n, x, y, number, k):
    operations = 0
    for i in range(n-k):
        if number[i] != number[i+k]:
            operations += 1
    return operations

def main():
    n, x, y = map(int, input().split())
    number = input()
    k = x - y
    print(solve(n, x, y, number, k))

if __name__ == "__main__":
    main()
