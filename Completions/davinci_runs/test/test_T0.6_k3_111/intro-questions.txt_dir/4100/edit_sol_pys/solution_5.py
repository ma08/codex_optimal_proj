

def solve(n, k, q, a):
    p = [k] * n
    for i in a: p[i-1] += 1

    for i in p: print('Yes' if i > q else 'No')

if __name__ == '__main__':
    n, k, q = map(int, input().split())
    a = [int(input()) for _ in range(q)]
    solve(n, k, q, a)
