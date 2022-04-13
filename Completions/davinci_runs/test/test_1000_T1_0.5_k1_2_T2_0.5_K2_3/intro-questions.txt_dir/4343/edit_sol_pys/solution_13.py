
def main():
    k = int(input())  # length of string
    s = input()  # start string
    t = input()  # end string
    if s == t:  # if start and end string are same
        print(s)  # print start string
        return
    if k == 1:  # if length of string is 1
        print(s)
        return
    if k == 2:
        if s[0] == t[0]:
            print(s[0] + chr(ord(s[1]) + 1))
            return
        else:
            print(s[0] + chr(ord(s[0]) + 1))
            return
    ans = [s]
    while True:
        if len(ans) == int((k + 1) / 2):
            break
        if ans[-1] == t:
            break
        if ans[-1][-1] == 'z':
            ans.append(ans[-1][:-1] + 'a')
        else:
            ans.append(ans[-1][:-1] + chr(ord(ans[-1][-1]) + 1))
    print(ans[-1])

main()
