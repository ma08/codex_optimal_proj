
N = int(input())

words = []
for i in range(N):
    words.append(input())

for i in range(1, N): # 1からNまで
    if words[i] in words[:i] or words[i][0] != words[i - 1][-1]: # words[i]がwords[:i]の中にあるか、words[i][0]がwords[i-1][-1]と同じではないか
        print("No")
        exit()

print("Yes")
