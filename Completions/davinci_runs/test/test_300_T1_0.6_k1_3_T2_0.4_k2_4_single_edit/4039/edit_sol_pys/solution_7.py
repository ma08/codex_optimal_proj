

def main():
    n, r = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    l_ = [r]
    for i in range(n):
        l_.append(l_[i]+b[i])
    l_ = l_[1:]
    for i in range(n):
        if a[i] > l_[i]:
            print("NO")
            return
    print("YES")
    return

if __name__ == '__main__':
    main()
