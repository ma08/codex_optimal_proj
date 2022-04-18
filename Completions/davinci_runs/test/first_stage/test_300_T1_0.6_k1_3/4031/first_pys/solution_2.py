
def solution(n, strings):
    substrings = []
    for i in strings:
        for j in strings:
            if i in j:
                substrings.append(i)
    if len(substrings) == len(strings):
        return "YES", substrings
    else:
        return "NO"

n = int(input())
strings = []
for i in range(n):
    strings.append(input())

print(solution(n, strings))