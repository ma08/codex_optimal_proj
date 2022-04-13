s = list(map(int, input().split()))
t = list(map(int, input().split()))

correct = 0

for i in range(len(s)):
    if s[i] == t[i]:
        correct += 1

print(correct)
