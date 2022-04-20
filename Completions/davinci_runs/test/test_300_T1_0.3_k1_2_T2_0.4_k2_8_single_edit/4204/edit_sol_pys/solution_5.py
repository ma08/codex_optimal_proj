

s = input()
k = int(input())

def next_day(s):
    next_s = ""
    for c in s:
        next_s += c * int(c)
    return next_s

for i in range(k):
    s = next_day(s)

print(s)
