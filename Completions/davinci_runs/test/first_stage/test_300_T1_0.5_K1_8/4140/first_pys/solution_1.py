

# Answer
S = input()

# 右隣が同じ色なら1を足す
cnt = 0
for i in range(len(S)-1):
    if S[i] == S[i+1]:
        cnt += 1

print(cnt)