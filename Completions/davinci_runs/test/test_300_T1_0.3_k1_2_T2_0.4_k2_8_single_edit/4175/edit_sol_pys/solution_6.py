
N = int(input())
words = []
for i in range(N):
    words.append(input().lower())

for i in range(N-1):
    if words[i] == words[i+1] or words[i][-1] != words[i+1][0]:
        print("No")
        exit()

print("Yes")
