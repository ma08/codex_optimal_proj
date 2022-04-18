
def main():
    k = int(input()) # length of string
    s = input() # start string
    t = input() # end string
    ans = []
    ans.append(s)
    while True:
        if len(ans) == int((k + 1) / 2):
            break
        if ans[-1] == t:
            break
        if ans[-1][-1] == 'z':
            ans.append(ans[-1][:-1] + 'a')
        else:
            ans.append(ans[-1][:-1] + chr(ord(ans[-1][-1]) + 1))
    if len(ans) == 1:
        print(s)
    else:
        print(ans[-1])

main()
