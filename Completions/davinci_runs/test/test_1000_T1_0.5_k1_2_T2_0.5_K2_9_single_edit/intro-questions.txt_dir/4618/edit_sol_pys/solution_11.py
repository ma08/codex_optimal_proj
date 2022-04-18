
s = input()
k = int(input())
substr = []
for i in range(len(s)):
    for j in range(i+1, len(s)+1):
        substr.append(s[i:j])
substr.sort()
print(substr[k-1])
