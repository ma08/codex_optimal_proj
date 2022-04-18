

def solve(a, b, c):
    return max(a, b, c) - min(a, b, c)

if __name__ == '__main__':
    a, b, c = map(int, input().split())
    print(solve(a, b, c))
