

n = int(input())
s = input()

for i in range(len(s)):
    print(chr((ord(s[i]) - ord('A') + n) % 26 + ord('A')), end = '')