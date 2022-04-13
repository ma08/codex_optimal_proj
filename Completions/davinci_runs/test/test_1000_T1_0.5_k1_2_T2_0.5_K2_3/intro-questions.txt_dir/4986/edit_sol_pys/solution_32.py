
def main():
    s = raw_input()
    t = raw_input()
    i = 0
    ans = ''
    while i < len(s):
        if s[i] == t[i*2]:
            ans += s[i]
        i += 1
    print(ans)

main()
