

# S = input()
S = "apple"

if S[-1] == "s":
    print(S + "es")
elif S[-1] == "o":
    print(S + "es")
elif S[-1] == "h" and S[-2] == "c":
    print(S + "es")
elif S[-1] == "f":
    print(S[:-1] + "ves")
elif S[-1] == "e" and S[-2] == "f":
    print(S[:-2] + "ves")
elif S[-1] == "y" and S[-2] != "a" and S[-2] != "i" and S[-2] != "u" and S[-2] != "e" and S[-2] != "o":
    print(S[:-1] + "ies")
else: 
    print(S + "s")
