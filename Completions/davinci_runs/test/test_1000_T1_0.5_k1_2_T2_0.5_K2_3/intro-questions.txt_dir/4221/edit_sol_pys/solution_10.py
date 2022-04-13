

S = input()
# S = "apple"

if S[-1] == "e":
    if S[-2] == "f":
        print(S + "s")
    else:
        print(S + "s")
else:
    if S[-1] == "f":
        print(S[:-1] + "ves")
    elif S[-2] == "f":
        print(S[:-2] + "ves")
    elif S[-1] == "o":
        print(S + "es")
    elif S[-2] == "o":
        print(S + "es")
    elif S[-1] == "y":
        print(S[:-1] + "ies")
    else:
        print(S + "s")
