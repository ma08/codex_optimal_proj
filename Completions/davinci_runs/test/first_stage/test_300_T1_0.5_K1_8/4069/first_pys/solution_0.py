

def solve(x, k, d):
    return max(0, abs(x) - k * d)

def main():
    x, k, d = [int(x) for x in input().split()]
    print(solve(x, k, d))

if __name__ == '__main__':
    main()