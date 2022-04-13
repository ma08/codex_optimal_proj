
def main():
    k = int(input())
    s = input()
    t = input()
    if s == t:
        print(s)
        return
    ans = []
    ans.append(s)
    while True:
        if len(ans) == int((k + 1) // 2):
            break
        if ans[-1] == t:
            break
        if ans[-1][-1] == 'z':
            ans.append(ans[-1][:-1] + 'a')
        else:
            ans.append(ans[-1][:-1] + chr(ord(ans[-1][-1]) + 1))
    print(ans[-1])

main()
