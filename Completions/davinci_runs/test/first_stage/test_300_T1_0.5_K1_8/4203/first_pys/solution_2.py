

#S = input()
S = "AtCoder"

flag = 1

if S[0] == "A":
    if S[2:len(S)-1].count("C") == 1:
        for i in range(len(S)):
            if i == 0 or i == 2:
                continue
            if S[i].islower():
                continue
            else:
                flag = 0
                break
    else:
        flag = 0
else:
    flag = 0

if flag == 1:
    print("AC")
else:
    print("WA")