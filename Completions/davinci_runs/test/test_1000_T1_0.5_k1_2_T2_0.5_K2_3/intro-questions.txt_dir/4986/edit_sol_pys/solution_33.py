

def main():
    s = input()
    t = input()
    i = 0;
    j = 0;
    ans = ""
    while i < len(s):
        if s[i] == t[j]:
            j += 2
            ans += s[i]
        i += 1
    print(ans)

main()
