

S = input()
T = input()
if S == T:
    print("Yes")
else:
    for i in range(len(S)):
        S = S[-1] + S[:-1]
        if S == T:
            print("Yes")
            exit()
    print("No")