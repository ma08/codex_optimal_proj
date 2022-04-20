

def solve(n, a, b):
    return sum(1 for x, y in zip(a, b) if x == -y)

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(solve(n, a, b))