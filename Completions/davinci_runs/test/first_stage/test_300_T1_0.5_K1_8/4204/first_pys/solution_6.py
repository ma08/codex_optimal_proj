

s = input()
k = int(input())

def f(s):
    ans = ""
    for i in s:
        ans += str(int(i) * int(i))
    return ans

for i in range(15):
    s = f(s)

print(s[k - 1])