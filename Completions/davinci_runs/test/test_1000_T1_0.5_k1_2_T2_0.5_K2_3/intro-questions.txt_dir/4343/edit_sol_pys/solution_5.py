def main():
    k = int(input())
    s = input()
    t = input()
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
    ans.append(s)
    while True:
        if len(ans) == int((k + 1) / 2):
            break
        if ans[-1][:-1] == t[:-1]:
            break
        if ans[-1][-1] == 'z' or ans[-1][-1] == 'Z':
            ans.append(ans[-1][:-1] + 'a')
        else:
            ans.append(ans[-1][:-1] + chr(ord(ans[-1][-1]) + 1))
    print(ans[-1])

main()
