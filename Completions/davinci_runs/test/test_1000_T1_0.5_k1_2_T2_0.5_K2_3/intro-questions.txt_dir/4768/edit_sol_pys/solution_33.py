n = int(input())
s = input()
i = 0
j = 1
count = 0
while i < n-1:
    while j < n:
        if s[i] == s[j]:
            count += 1
            i += 1
            j += 1
        else:
            i += 1
            j += 1
    i += 1
    j += 1
print(count)
