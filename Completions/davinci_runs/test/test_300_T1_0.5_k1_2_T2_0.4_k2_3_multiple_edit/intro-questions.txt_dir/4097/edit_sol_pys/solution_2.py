import sys

def main():
    n = int(input())
    arr = list(map(int,input().split()))
    d = arr[1] - arr[0]
    ans = 0
    for i in range(2,n):
        if arr[i] - arr[i-1] != d:
            ans += 1
    if ans > 2:
        print(-1)
    else:
        print(ans)

if __name__ == "__main__":
    main()
