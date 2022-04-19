

s = input()
t = input()
current_s = 0
current_t = 0
count = 0
for i in range(len(s)):
    if s[i] == t[i]:
        count += 1
    else:
        if s[i] == "0":
            current_s += 1
        else:
            current_t += 1

print(count)
