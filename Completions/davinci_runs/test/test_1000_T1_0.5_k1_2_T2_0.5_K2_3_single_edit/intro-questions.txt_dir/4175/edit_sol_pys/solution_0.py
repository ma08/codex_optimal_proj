
N = int(input())

words = []
for _ in range(N):
    words.append(input().strip())
if len(set(words)) != N:
    print("No")
    exit()
if len(set(words[i][0] for i in range(N))) == 1:
    print("No")
    exit()
if len(set(words[i][-1] for i in range(N))) == 1:
    print("No")
    exit()
if len(set(words[i][0] for i in range(1, N))) != N - 1:
    print("No")
    exit()
if len(set(words[i][-1] for i in range(N - 1))) != N - 1:
    print("No")
    exit()
for i in range(N - 1):
    if words[i][-1] != words[i + 1][0]:
        print("No")
        exit()
print("Yes")    
