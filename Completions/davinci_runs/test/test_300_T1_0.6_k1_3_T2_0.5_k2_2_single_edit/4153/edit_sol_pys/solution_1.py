

n = int(input())
s = input()

count = 0
while s:
    if s[0] == '0':
        count += 1
        s = s[1:]
    elif s[0] == '1':
        if len(s) > 1 and s[1] == '0':
            count += 1
            s = s[2:]
        else:
            break

print(count)
