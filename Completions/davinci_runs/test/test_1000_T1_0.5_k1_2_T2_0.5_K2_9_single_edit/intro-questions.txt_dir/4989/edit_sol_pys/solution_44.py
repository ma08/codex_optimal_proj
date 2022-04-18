

def main():
    n, k, q = map(int, input().split())
    a = [int(input()) for _ in range(q)]
    ans = [0] * n
    for ai in a:
        ans[ai - 1] += 1
    for an in ans:
        if an - k >= 0:
            print('No')
        else:
            print('Yes')

main()
