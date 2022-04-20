

S = input()
K = int(input())
#S = "1214"
#K = 4

def replace(S):
    S = list(S)
    for i in range(len(S)):
        if S[i] == "2":
            S[i] = "22"
        elif S[i] == "3":
            S[i] = "333"
        elif S[i] == "4":
            S[i] = "4444"
        elif S[i] == "5":
            S[i] = "55555"
        elif S[i] == "6":
            S[i] = "666666"
        elif S[i] == "7":
            S[i] = "7777777"
        elif S[i] == "8":
            S[i] = "88888888"
        elif S[i] == "9":
            S[i] = "999999999"
    return "".join(S)

for i in range(15):
    S = replace(S)

print(S[K-1])
