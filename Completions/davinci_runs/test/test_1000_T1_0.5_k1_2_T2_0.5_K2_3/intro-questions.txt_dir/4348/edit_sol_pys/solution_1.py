

# SOLUTION

n, k = map(int, input().split())
s = input()

for i in range(k):
    for i in range(26):
        if chr(i+97) in s:
            s = s[s.find(chr(i+97))+1:]
print(s)
