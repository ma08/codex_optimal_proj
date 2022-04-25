

S = input()
# S = "apple"

if S[-1] == "s" or S[-1] == "o" or S[-1] == "x" or S[-1] == "z":
    print(S + "es", end="")
elif S[-1] == "h" and S[-2] == "c":
    print(S + "es", end="")
elif S[-1] == "h" and S[-2] == "s":
    print(S + "es", end="")
elif S[-1] == "h" and S[-2] == "o":
    print(S + "es", end="")
elif S[-1] == "f" and S[-2] == "f":
    print(S[:-1] + "ves", end="")
elif S[-1] == "f" and S[-2] == "e":
    print(S[:-1] + "ves", end="")
elif S[-1] == "e" and S[-2] == "f":
    print(S[:-1] + "ves", end="")
elif S[-1] == "y" and S[-2] == "a":
    print(S[:-1] + "ies", end="")
elif S[-1] == "y" and S[-2] == "i":
    print(S[:-1] + "ies", end="")
elif S[-1] == "y" and S[-2] == "u":
    print(S[:-1] + "ies", end="")
elif S[-1] == "y" and S[-2] == "o":
    print(S[:-1] + "ies", end="")
elif S[-1] == "y" and S[-2] == "e":
    print(S[:-1] + "ies", end="")
else:
    print(S + "s", end="")
