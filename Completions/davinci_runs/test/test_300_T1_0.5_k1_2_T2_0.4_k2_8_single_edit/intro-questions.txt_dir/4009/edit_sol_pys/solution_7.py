

def solve(n, m, a, b):
    if n == 1:
        return a
    if m == 1:
        return b
    if n == 2:
        return min(2*a, b)
    if m == 2:
        return min(2*b, a)
    return min(2*a, 2*b, a+b)

def main():
    n, m = map(int, input().split())
    a, b = map(int, input().split())
    print(solve(n, m, a, b))

if __name__ == "__main__":
    main()
