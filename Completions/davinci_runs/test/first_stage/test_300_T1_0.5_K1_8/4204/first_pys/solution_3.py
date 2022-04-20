

s = input()
k = int(input())

count = 0
for i in range(len(s)):
    if s[i] == '1':
        count += 1
    elif s[i] == '2':
        count += 2
    elif s[i] == '3':
        count += 3
    elif s[i] == '4':
        count += 4
    elif s[i] == '5':
        count += 5
    elif s[i] == '6':
        count += 6
    elif s[i] == '7':
        count += 7
    elif s[i] == '8':
        count += 8
    elif s[i] == '9':
        count += 9

if count < k:
    print('No')
else:
    print('Yes')