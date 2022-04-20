


def solve(n, l):
    ans = 0
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if l[i] < l[j] + l[k] and l[j] < l[i] + l[k] and l[k] < l[i] + l[j]:
                    ans += 1
    return ans

def main():
    n = int(input())
    l = list(map(int, input().split()))
    ans = solve(n, l)
    print(ans)

if __name__ == '__main__':
    main()
