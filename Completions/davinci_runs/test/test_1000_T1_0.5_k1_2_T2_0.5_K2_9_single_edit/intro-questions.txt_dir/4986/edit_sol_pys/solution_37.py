

def main():
    s = input()
    t = input()
    i = 0
    ans = ''
    while i < len(s):
        if s[i] == t[i*2]: # i*2 is the index of the same char in t
            ans += s[i]
        i += 1
    print(ans)

main()
