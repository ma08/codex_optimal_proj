

def main():
    H, n = map(int, input().split())
    d = list(map(int, input().split()))
    d.append(H)
    d.sort()
    # print(d)
    if d[0] > 0:
        print(-1)
        return
    if d[0] == 0:
        print(1)
        return
    if d[0] == d[-1]:
        print(H//d[0] + 1)
        return
    ans = 0
    for i in range(n):
        if d[i] < 0:
            ans += d[i]
    ans = -ans
    # print(ans)
    if ans <= H:
        print(ans)
        return
    if d[0] < 0:
        print(-1)
        return
    for i in range(n):
        if d[i] >= 0:
            ans = d[i]
            break
    ans = ans * (H//ans) + 1
    print(ans)
    return

if __name__ == '__main__':
    main()