

n = int(input())
words = [input() for i in range(n)]

for i in range(1,n):
    if words[i] in words[:i] or words[i][0] != words[i-1][-1]:
        print("No")
        exit()



# 短く書くと
print(["No","Yes"][all(w not in words[:i] and w[0] == words[i-1][-1] for i,w in enumerate(words[1:],1))])
print("Yes")
