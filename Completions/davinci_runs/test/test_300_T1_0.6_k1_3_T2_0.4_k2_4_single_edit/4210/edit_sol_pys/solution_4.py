

def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 1
    for i in range(n):
        for j in range(i + 1, n):
            if (a[i] + a[j]) % k == 0:
                ans += 1
    return ans - 1

def main():
    print(solve())
    
if __name__ == '__main__':
    main()
