

def solve(n, x, y, s):
    operations = 0
    for i in range(n-x):
        if s[i] != s[i+x-y]:
            operations += 1
    return operations

def main():
    n, x, y = map(int, input().split())
    s = input()
    print(solve(n, x, y, s))

if __name__ == "__main__":
    main()
