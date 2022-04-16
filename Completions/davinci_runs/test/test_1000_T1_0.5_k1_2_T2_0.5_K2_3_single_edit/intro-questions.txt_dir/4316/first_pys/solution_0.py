

#-----main-----

S = input()

#-----check-----

if len(S) == 4:
    if S[0] == S[1] and S[2] == S[3]:
        if S[0] != S[2]:
            print("Yes")
        else:
            print("No")
    elif S[0] == S[2] and S[1] == S[3]:
        if S[0] != S[1]:
            print("Yes")
        else:
            print("No")
    elif S[0] == S[3] and S[1] == S[2]:
        if S[0] != S[1]:
            print("Yes")
        else:
            print("No")
    else:
        print("No")
else:
    print("No")