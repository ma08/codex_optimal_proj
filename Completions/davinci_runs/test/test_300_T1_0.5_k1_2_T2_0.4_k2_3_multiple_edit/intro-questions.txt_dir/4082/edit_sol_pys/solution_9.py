

def main():
    n, m = map(int, input().split())
    a = list(map(lambda x: int(x) - 1, input().split()))
    ans = [0] * n
    for i in range(m):
        ans[a[i]] += 1
    print(ans.index(max(ans)) + 1)

if __name__ == '__main__':
    main()
