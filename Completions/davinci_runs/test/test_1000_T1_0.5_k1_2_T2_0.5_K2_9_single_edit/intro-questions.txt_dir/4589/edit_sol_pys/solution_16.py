

#%%
# H, W = list(map(int, input().split()))
H, W = 3, 5
# S = [input() for _ in range(H)]
S = ['.....', '.#.#.', '.....']
# i, j = 0, 0
# print('i =', i)
# print('j =', j)
# print('S[i][j] =', S[i][j])
# print('S[i][j-1] =', S[i][j-1])
# print('S[i][j+1] =', S[i][j+1])
# print('S[i-1][j] =', S[i-1][j])
# print('S[i-1][j-1] =', S[i-1][j-1])
# print('S[i-1][j+1] =', S[i-1][j+1])
# print('S[i+1][j] =', S[i+1][j])
# print('S[i+1][j-1] =', S[i+1][j-1])
# print('S[i+1][j+1] =', S[i+1][j+1])

for i in range(H):
    for j in range(W):
        if S[i][j] == '.':
            cnt = 0
            if j > 0:
                cnt += 1 if S[i][j-1] == '#' else 0
            if j < W-1:
                cnt += 1 if S[i][j+1] == '#' else 0
            if i > 0:
                cnt += 1 if S[i-1][j] == '#' else 0
            if i < H-1:
                cnt += 1 if S[i+1][j] == '#' else 0
            if i > 0 and j > 0:
                cnt += 1 if S[i-1][j-1] == '#' else 0
            if i > 0 and j < W-1:
                cnt += 1 if S[i-1][j+1] == '#' else 0
            if i < H-1 and j > 0:
                cnt += 1 if S[i+1][j-1] == '#' else 0
            if i < H-1 and j < W-1:
                cnt += 1 if S[i+1][j+1] == '#' else 0
            S[i] = S[i][:j] + str(cnt) + S[i][j+1:]

print('\n'.join(S))

# S = ['.....', '.#.#.', '.....']
# print(S[0][0])
# print(S[0][0:0])
# print(S[0][0+1:])
# print(S[0][0:0] + '1' + S[0][0+1:])
# print(S[0][0:1] + '1' + S[0][1+1:])
# print(S[0][0:2] + '1' + S[0][2+1:])
# print(S[0][0:3] + '1' + S[0][3+1:])
# print(S[0][0:4] + '1' + S[0][4+1:])
# print(S[0][0:5] + '1' + S[0][5+1:])

#%%
# S = ['.....', '.#.#.', '.....']
# print(S[0][0])
# print(S[1][0])
# print(S[2][0])
# print(S[0][1])
# print(S[1][1])
# print(S[2][1])
# print(S[0][2])
# print(S[1][2])
# print(S[2][2])
# print(S[0][3])
# print(S[1][3])
# print(S[2][3])
# print(S[0][4])
# print(S[1][4])
# print(S[2][4])

#%%
