
S = str(input())
T = str(input())

if S == T:
    print("Yes")
    exit()
for _ in range(len(S)-1):
    S = S[-1] + S[:-1]
    if S == T:
        print("Yes")
        exit()
print("No")
