
#Solution
def solution(a, f):
    a = list(map(int, a.split()))
    f = list(map(int, f.split()))
    ans = 0

    for i in range(0, len(a)):
        ans += max(f[a[i]-1:a[i]+1]) * 10**(len(a) - i - 1)

    return ans

#Test Cases
test1 = '1337'
test2 = '1 2 5 4 6 6 3 1 9'

print(solution(test1, test2))
