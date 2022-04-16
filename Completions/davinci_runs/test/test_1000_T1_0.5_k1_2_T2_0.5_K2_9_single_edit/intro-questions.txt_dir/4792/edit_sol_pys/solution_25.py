

def delete_duplicates(s):
    i = 0
    while i < len(s) - 1:
        if s[i] == s[i + 1]:
            s = s[:i + 1] + s[i + 2:]
        else:
            i += 1
    return s
    
s = input()
s = list(s)
s.sort()
s = "".join(s)
s = delete_duplicates(s)
print(s)
n = len(s)
i = 1
while i < n:
    if s[i] == s[i - 1]:
        i += 1
    else:
        print(s[i - 1], end="")
        i += 2
if i == n:
    print(s[n - 1], end="")
