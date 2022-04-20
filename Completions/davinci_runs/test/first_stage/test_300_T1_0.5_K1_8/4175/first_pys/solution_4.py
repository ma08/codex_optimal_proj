

N = int(input())
words = []
for i in range(N):
    words.append(input())

if len(words) == len(set(words)):
    for i in range(1, N):
        if words[i-1][-1] != words[i][0]:
            print("No")
            exit()
    print("Yes")
else:
    print("No")