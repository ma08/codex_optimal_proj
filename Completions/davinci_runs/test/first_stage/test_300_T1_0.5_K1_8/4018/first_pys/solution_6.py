

def main():
    n,k = map(int,input().split())
    string = input()
    ans = 0
    for i in range(n):
        ans += n-i
    if k > ans:
        print("-1")
    else:
        print(ans-k)


main()