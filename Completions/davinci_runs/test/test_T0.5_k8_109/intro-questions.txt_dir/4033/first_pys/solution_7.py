

def main():
    a, b = map(int, input().split())
    print(solve(a, b))

def solve(a, b):
    if a < b:
        a, b = b, a
    if a >= 2*b:
        return 2*(a+b)
    return 2*a + 2*b - a

if __name__ == '__main__':
    main()