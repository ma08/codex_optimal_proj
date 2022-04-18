

N = int(input())
S = input()

max_count = 0
max_gram = ""
for i in range(N-1):
    gram = S[i:i+2]
    if S.count(gram) > max_count:
        max_count = S.count(gram)
        max_gram = gram
print(max_gram)
