

def main():
    n = int(input())
    s = input()
    t = input()
    if s == t:
        print("0")
        return
    if len(set(s)) == 1:
        print("-1")
        return
    r = []
    for i in range(n):
        if s[i] != t[i]:
            if s[i+1] != t[i] and i+1 < n:
                r.append(i+1)
                s = s[:i] + s[i+1] + s[i] + s[i+2:]
            else:
                r.append(i)
                s = s[:i] + s[i+1] + s[i] + s[i+2:]
    if s != t:
        print("-1")
        return
    else:
        print(len(r))
        print(*r)

if __name__ == "__main__":
    main()