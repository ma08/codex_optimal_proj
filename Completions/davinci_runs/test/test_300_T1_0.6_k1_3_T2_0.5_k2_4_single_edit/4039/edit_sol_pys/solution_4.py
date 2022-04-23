

def main():
    n, r = map(int, input().split()) #n:問題数,r:初期値
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai) #ai:問題難易度
        b.append(bi) #bi:問題得点
    l = [r]
    for i in range(n):
        l.append(l[i]+b[i])
    l = l[1:]
    for i in range(n):
        if a[i] > l[i]:
            print("NO")
            return
    print("YES")
    return

if __name__ == '__main__':
    main()
