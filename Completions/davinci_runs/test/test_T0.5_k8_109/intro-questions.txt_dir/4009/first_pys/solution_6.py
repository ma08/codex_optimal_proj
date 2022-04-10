

def main():
    n,x,y = map(int,input().split())
    num = input()
    num = list(num)
    ans = 0
    for i in range(n-1,x-1,-1):
        if num[i] != '1':
            ans += 1
        else:
            break
    for i in range(x-1,y-1,-1):
        if num[i] != '0':
            ans += 1
        else:
            break
    print(ans)

main()