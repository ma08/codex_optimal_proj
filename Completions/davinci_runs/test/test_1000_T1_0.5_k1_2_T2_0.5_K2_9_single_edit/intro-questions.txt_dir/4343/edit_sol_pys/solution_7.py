
def main():
    k = int(input())
    s = input()
    t = input()
    if s == t:
        print(s)
        return
    if k == 1:
        print(s)
        return
    if k == 2:
        if s[0] == t[0]:
            print(s[0] + chr(ord(s[1]) + 1))
            return
        else:
            print(s[0] + chr(ord(s[0]) + 1))
            return
    ans = []
    while True:
        if len(ans) == int((k + 1) / 2) or ans[-1] == t:
            break
        if s[-1] == 'z':
            ans.append(s[:-1] + 'a')
        else:
            ans.append(s[:-1] + chr(ord(s[-1]) + 1))
    print(ans[-1])

main()
