
import sys

def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    c = [int(i) for i in input().split()]
    prev = -1
    ans = 0
    for i in range(n):
        if prev+1 == a[i]:
            ans += c[prev-1]
        ans += b[a[i]-1]
        prev = a[i]
    print(ans)

if __name__ == "__main__":
    main()
