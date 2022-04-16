
def main():
    k = int(input())
    s = input()
    t = input()
    ans = []
    while True:
        ans.append(s)
        if len(ans) == k:
            break
        s = s[-1] + s[:-1]
    for i in range(len(ans)):
        print(ans[i])

main()
