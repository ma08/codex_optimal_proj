

n = int(input())
s = input()

if s == ''.join(sorted(s)):
    print('YES')
    print('0'*n)
    exit()

if s == ''.join(sorted(s)[::-1]):
    print('YES')
    print('1'*n)
    exit()

# print(s)
# print(''.join(sorted(s)))
# print(''.join(sorted(s)[::-1]))

for i in range(1, n-1):
    if s[i] == s[i-1]:
        continue
    if s[i] == s[i+1]:
        continue
    if s[i] < s[i-1]:
        s = s[:i-1] + s[i] + s[i-1] + s[i+1:]
        break
    else:
        s = s[:i] + s[i+1] + s[i] + s[i+2:]
        break

# print(s)
# print(''.join(sorted(s)))
# print(''.join(sorted(s)[::-1]))

if s == ''.join(sorted(s)) or s == ''.join(sorted(s)[::-1]):
    print('YES')
    print('0'*(i-1) + '1' + '0'*(n-i-1))
else:
    print('NO')