

def main():
    s = input()
    t = input()
    i = 0
    ans = []
    while i < len(s):
        if s[i] == t[i*2]:
            ans.append(s[i])
        i += 1
    print(''.join(ans))

main()
