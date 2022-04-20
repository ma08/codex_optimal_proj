

def main():
    n = int(input())
    a = list(map(int, input().split()))    

    ans = [0] * n
    for i in range(1, n):
        ans[i] = min(ans[i-1] + abs(a[i] - a[i-1]), ans[i-2] + abs(a[i] - a[i-2]))

    print(ans[-1])

if __name__ == '__main__':
    main()
