

def main():
    n = int(input())
    s = input()
    t = input()

    if len(set(s+t)) != 3:
        print("NO")
        return

    res = ""
    for i in range(n):
        res += s[0] + t[0] + s[1] + t[1]
    res = res.replace(s[0], "")
    res = res.replace(s[1], "")
    res = res.replace(t[0], "")
    res = res.replace(t[1], "")

    print("YES")
    print(res)


main()