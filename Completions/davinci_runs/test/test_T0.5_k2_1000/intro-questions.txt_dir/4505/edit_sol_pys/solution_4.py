
S = input()

if sorted(S) == ['a', 'b', 'c'] or sorted(S) == ['a', 'c', 'b'] or sorted(S) == ['b', 'a', 'c'] or sorted(S) == ['b', 'c', 'a'] or sorted(S) == ['c', 'a', 'b'] or sorted(S) == ['c', 'b', 'a']:
    print('Yes')
else:
    print('No')
