

def solve(n, a, b):
    ans = 1
    for i in range(1, n - 1):
        if a[i] < a[i - 1] and b[i] < b[i + 1]:
            ans += 1
        else:
            break
    # for i in range(n - 2, -1, -1):
    #     if a[i] < a[i + 1]:
    #         ans += 1
    #     else:
    #         break
    return ans

def main():
    n = int(input())
    b = list(map(int, input().split()))
    print(solve(n, a, b))

if __name__ == "__main__":
    main()
