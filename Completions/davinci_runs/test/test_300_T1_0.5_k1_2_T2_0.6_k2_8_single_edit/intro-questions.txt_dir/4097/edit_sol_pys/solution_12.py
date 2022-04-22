
import sys

def main():
    n = int(sys.stdin.readline())
    arr = list(map(int,sys.stdin.readline().split()))
    if n == 1:
        print(0)
        return
    elif n == 2:
        if arr[0] == arr[1]:
            print(0)
        else:
            print(1)
        return
    else:
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
