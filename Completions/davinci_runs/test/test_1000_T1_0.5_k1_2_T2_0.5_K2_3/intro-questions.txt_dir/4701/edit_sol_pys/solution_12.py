

def solve(n):
    if n == 1:
        return 1
    return solve(n-1) + solve(n-2)

if __name__ == '__main__':
    n = int(input())
    print(solve(n))
