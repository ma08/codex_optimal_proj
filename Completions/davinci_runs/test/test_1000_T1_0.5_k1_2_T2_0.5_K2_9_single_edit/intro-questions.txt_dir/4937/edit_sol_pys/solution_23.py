import math



def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n-1):
        if a[i] == a[i+1]:
            ans += 1
    print(ans)

main()
