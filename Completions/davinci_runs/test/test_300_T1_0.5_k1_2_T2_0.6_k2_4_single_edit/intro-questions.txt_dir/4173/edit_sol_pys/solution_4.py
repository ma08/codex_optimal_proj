

n = int(input())
s = input()
a = s.count('A')
d = n - a
if a > d:
    print('Anton')
elif d > a:
    print('Danik')
else:
    print('Friendship')
