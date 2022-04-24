

n = int(input())
s = input()

max_count = 0
max_gram = ""
for i in range(n-1):
    gram = s[i:i+2]
    if s.count(gram) > max_count:
        max_count = s.count(gram)
        max_gram = gram
print(max_gram)
