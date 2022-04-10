

def main():
    n = int(input())
    s = input()
    t = input()
    a, b, c = [], [], []
    if s[0] == s[1]:
        a.append(s[0])
        b.append(t[0])
        c.append(t[1])
    elif t[0] == t[1]:
        a.append(t[0])
        b.append(s[0])
        c.append(s[1])
    else:
        a.append(s[0])
        b.append(s[1])
        c.append(t[0])
        a.append(t[1])

    for i in range(n-1):
        a.append(b[-1])
        b.append(c[-1])
        c.append(a[-1])

    print("YES")
    print("".join(a+b+c))

if __name__ == "__main__":
    main()