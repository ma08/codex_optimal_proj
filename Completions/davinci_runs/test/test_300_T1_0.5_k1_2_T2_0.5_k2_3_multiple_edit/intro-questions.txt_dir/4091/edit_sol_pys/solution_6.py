
def main():
    n = int(input())
    s = input()
    ans = 0
    for i in range(n):
        if s[i] == 'E':
            ans += 1
    ans = 0
    ans = min(ans,n-ans)
    print(ans)

main()
