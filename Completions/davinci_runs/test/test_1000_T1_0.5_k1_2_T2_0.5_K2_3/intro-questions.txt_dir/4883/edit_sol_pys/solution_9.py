# https://codeforces.com/problemset/problem/1271/B

def main():
    n, k = [int(x) for x in input().split()]
    s = input()
    if k == 1:
        print(s)
        return
    if len(s) == 1:
        print(s)
        return
    if s[0] != '1':
        print(s[0])
        print(s[1:])
        return
    ans = ["1"]
    for i in range(1, len(s)):
        if s[i] != '0':
            ans.append(s[i])
            break
    ans.extend(["0"] * (len(s) - len(ans)))
    print("".join(ans))

if __name__ == '__main__':
    main()
