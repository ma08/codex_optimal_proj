

def main():
    n = int(input())
    s = input()
    if s == "b":
        print(0)
        return
    ans = 0
    while s != "b":
        if s[-3:] == "aaa":
            s = s[:-3]+"b"
        elif s[-2:] == "aa":
            s = s[:-2]+"b"
        elif s[-1] == "a":
            s = s[:-1]+"b"
        ans += 1
    print(ans)

if __name__ == '__main__':
    main()
