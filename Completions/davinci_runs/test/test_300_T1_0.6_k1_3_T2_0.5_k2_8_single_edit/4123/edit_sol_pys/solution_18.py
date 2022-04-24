

n = int(input())
s = input()

count = 0
gram = ""
for i in range(n-1):
    gram_ = s[i:i+2]
    if s.count(gram_) > count:
        count = s.count(gram_)
        gram = gram_
print(gram)
