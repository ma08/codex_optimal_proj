
# https://atcoder.jp/contests/abc049/submissions/14093268
# https://atcoder.jp/contests/abc049/tasks/arc065_a

def main():
    s = input()
    t = input()
    i = 0
    ans = ''
    while i < len(s):
        if s[i] == t[i*2]:
            ans += s[i]
        i += 1
    print(ans)

main()
