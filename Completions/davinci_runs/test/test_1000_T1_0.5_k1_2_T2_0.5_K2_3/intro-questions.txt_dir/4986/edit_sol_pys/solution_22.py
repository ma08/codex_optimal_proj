
s = input().strip()  # strip() removes the leading and trailing spaces
t = input().strip()  # strip() removes the leading and trailing spaces

for i in range(len(s)):
    if s[i] != t[2 * i]:
        print(s[i], end='')
