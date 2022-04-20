

S = input()

for i in range(0, len(S), 2):
    if S[i] == 'L':
        print('No')
        exit()
for i in range(1, len(S), 2):
    if S[i] == 'R':
        print('No')
        exit()
print('Yes')