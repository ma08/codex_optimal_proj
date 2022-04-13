x = int(input())
s = input()

w = 0
m = 0
i = 0

for c in s:
    if c == 'W':
        w += 1
    else:
        m += 1
    if abs(w - m) > x:  # if the difference between w and m is greater than x
        break
    i += 1  # increment i

print(i)
