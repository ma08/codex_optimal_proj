

s = input()

odds = ['R', 'U', 'D']
evens = ['L', 'U', 'D']

for i in range(len(s)):
    if i % 2 == 0:
        if s[i] not in odds:
            print('No')
            exit()
    else:
        if s[i] not in evens:
            print('No')
            exit()

print('Yes')