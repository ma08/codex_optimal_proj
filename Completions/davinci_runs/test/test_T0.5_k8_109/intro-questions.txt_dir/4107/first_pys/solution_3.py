

def main():
    n,k = map(int,input().split())
    s = input()
    routers = [i for i in range(n) if s[i] == '1']
    ans = 0
    if len(routers) == 0:
        ans = sum(range(n))
    else:
        routers.append(n)
        routers.insert(0,0)
        for i in range(1,len(routers)):
            ans += min(routers[i] - routers[i-1],routers[i] - routers[i-1] - 1)
    print(ans)

if __name__ == "__main__":
    main()