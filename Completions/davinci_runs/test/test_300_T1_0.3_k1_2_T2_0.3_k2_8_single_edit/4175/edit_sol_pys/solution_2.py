
N = int(input())
words = []
for i in range(N):
    words.append(input())

for i in range(N-1):
    if words[i] == words[i+1] or words[i][-1] != words[i+1][0] or len(words[i]) != len(words[i+1]):
        print("No")
        exit()

print("Yes")
