

# My answer
s = input()

s_odd = s[1::2]
s_even = s[0::2]

if 'L' in s_odd or 'R' in s_even:
    print('No')
else:
    print('Yes')

# Official answer
s = input()
if any(c in 'LR' for c in s[::2]):
    print('No')
elif any(c in 'LR' for c in s[1::2]):
    print('No')
else:
    print('Yes')