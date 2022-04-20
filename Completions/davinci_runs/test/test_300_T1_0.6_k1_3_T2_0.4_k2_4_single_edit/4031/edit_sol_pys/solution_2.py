
def solution(n, strings):
    if n == 1:
        return "YES"
    else:
        return "NO"

n = int(input())
strings = []
for i in range(n):
    strings.append(input())

print(solution(n, strings))
