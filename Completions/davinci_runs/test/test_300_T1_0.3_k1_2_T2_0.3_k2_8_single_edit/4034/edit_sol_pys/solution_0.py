from collections import Counter

n = int(input())
s = input()

c = Counter(s)
if c['a'] > c['b']:
    print('b' * c['b'] + 'a' * (c['a'] - c['b']))
elif c['a'] < c['b']:
    print('a' * c['a'] + 'b' * (c['b'] - c['a']))
elif c['a'] == c['b']:
    print('ab' * c['a'])
