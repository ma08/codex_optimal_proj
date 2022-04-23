def main():
    n = int(input())
    a = list(map(int, input().split()))
    if n % 2 == 0:
        print("NO")
        return
    a.sort()
    for i in range(n//2):
        if a[i] != 2*(i+1) - 1 or a[n-i-1] != 2*(i+1):
            print("NO")
            return
    print("YES")
main()
