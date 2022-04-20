

def solve(a, b):
    return abs(a-b)

def main():
    a, b = map(int, input().split())
    print(solve(a, b))

if __name__ == '__main__':
    main()