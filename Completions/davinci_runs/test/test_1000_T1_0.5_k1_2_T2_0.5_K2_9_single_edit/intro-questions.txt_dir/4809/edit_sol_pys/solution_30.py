

n = int(input())
s = input()

a = s.count('A')
d = s.count('D')

if a > d:
    print('Anton')
elif a < d:
    print('Danik')
else:
    print('Friendship')
