

def main():
    s = input()
    t = input()
    i = 1
    ans = ''
    while i < len(t):
        if s[i] == t[i]:
            ans += '1'
        else:
            ans += '0'
        i += 1
    print(ans)

main()
