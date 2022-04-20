

N = int(input())
S = input()

count = 0
gram = ""
for i in range(N-1):
    gram = S[i:i+2]
    if S.count(gram) > count:
        count = S.count(gram)
        gram = gram
print(gram)
