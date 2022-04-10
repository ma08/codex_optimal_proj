
def main():
    n, r = map(int, input().split())
    a = []
    b = []
    for _ in range(n):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)

    for i in range(n):
        if r < a[i]: break
        r += b[i]
        if r < 0: break
    else:
        print("YES") 


if __name__ == '__main__':
    main()
