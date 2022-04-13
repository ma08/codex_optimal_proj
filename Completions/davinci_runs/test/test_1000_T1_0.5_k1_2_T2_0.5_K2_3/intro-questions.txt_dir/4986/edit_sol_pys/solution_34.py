

def main():
    s = input()
    t = input()
    i = 1
    ans = ""
    while i < len(s):
        if s[i] == t[i*2-1]:
            ans += s[i]
        i += 1
    print(ans)

main()
