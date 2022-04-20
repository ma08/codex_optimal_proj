
s = input()
k = int(input())

def next_day(s_):
    next_s_ = ""
    for c in s_:
        next_s_ += c * int(c)
    return next_s_

for i in range(15):
    s = next_day(s)

print(s[k-1])
