

#-----Solution-----
def solution(a, f):
    a = list(map(int, a))
    f = list(map(int, f))
    ans = 0

    for i in range(0, len(a)):
        ans += max(f[a[i]-1:a[i]+1]) * 10**(len(a) - i - 1)

    return ans

#-----Test-----
a = '1337'
f = '1 2 5 4 6 6 3 1 9'

print(solution(a, f))