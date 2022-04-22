

N = int(input())
S = input()
K = int(input())

for c in S:
    if c.islower():
        print(chr(((ord(c) - ord('a') + K) % 26) + ord('a')), end='')
    elif c.isupper():
        print(chr(((ord(c) - ord('A') + K) % 26) + ord('A')), end='')
    else:
        print(c, end='')
print()
