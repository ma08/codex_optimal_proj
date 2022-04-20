

#---Functions---
def check(S,T):
    if S == T:
        return True
    else:
        return False

def replace(S,T):
    for i in range(len(S)):
        if S[i] != T[i]:
            S = S.replace(S[i],T[i])
    return S

#---Main---
S = input()
T = input()

if check(S,T) == True:
    print("Yes")
else:
    S = replace(S,T)
    if check(S,T) == True:
        print("Yes")
    else:
        print("No")