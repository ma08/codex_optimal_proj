

n = int(input())

for i in range(n):
    s = input()

    if (len(s) % 2 == 0) and (s[0] in 'RUD') and (s[-1] in 'RUD'):
        print('Yes')
    else:
        print('No')
