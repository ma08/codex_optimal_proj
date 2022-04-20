

s = input()
k = int(input())

def next_day(s):
    result = ''
    for c in s:
        result += c * int(c)
    return result

for i in range(16):
    s = next_day(s)

print(s[k-1])