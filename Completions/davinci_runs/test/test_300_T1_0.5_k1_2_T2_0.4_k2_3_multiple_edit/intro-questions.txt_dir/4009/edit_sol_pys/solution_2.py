

def solve(n, x, y, number_):
    operations = 0
    for i in range(n - x):
        if number_[i] != number_[i+x-y]:
            operations += 1
    return operations

def main():
    n, x, y = map(int, input().split())
    number_ = input()
    print(solve(n, x, y, number_))

if __name__ == "__main__":
    main()
