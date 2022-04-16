

def solve(n, x, y, number, k):
    operations = 0
    for i in range(n-x+1):
        if number[i] != number[i+x-y-1]:
            operations += k
    return operations+k

def main():
    n, x, y, k = map(int, input().split())
    number = input()
    print(solve(n, x, y, number, k))

if __name__ == "__main__":
    main()
