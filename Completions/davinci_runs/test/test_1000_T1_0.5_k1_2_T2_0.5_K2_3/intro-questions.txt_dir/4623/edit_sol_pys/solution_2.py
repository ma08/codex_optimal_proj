# Problem Link: https://www.codechef.com/JUNE20B/problems/XYSTR

# SOLUTION
t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    ans = 1
    for i in range(1, n):
        if s[i] == s[i-1]:
            ans += 1
            i += 1
        else:
            continue
    ans = ans//2
    print(ans)
