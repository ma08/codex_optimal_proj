
def solve(n, a):
    ans = 0
    for i in range(1, n):
        if a[i] > a[i - 1]:
            ans += 1
        else:
            break
    for i in range(n - 2, -1, -1):
        if a[i] < a[i + 1]:
            ans += 1
        else:
            break
    return ans

def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(solve(n, a))

if __name__ == "__main__":
    main()
