

n = int(input())
s = input()

max_count = 0
for i in range(n-1):
    count = s.count(s[i:i+2])
    if count > max_count:
        max_count = count
        max_gram = s[i:i+2]

print(max_gram)