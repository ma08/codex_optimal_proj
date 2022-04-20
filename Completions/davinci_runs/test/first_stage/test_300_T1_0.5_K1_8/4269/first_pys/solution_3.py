

#1
S = input()
if S[0] == S[1] or S[1] == S[2] or S[2] == S[3]:
    print("Bad")
else:
    print("Good")

#2
S = input()
print("Bad" if S[0] == S[1] or S[1] == S[2] or S[2] == S[3] else "Good")

#3
S = input()
if (S[0] == S[1] or S[1] == S[2] or S[2] == S[3]) == True:
    print("Bad")
else:
    print("Good")

#4
S = input()
if (S[0] == S[1] or S[1] == S[2] or S[2] == S[3]) == False:
    print("Good")
else:
    print("Bad")

#5
S = input()
print("Bad" if S[0] == S[1] or S[1] == S[2] or S[2] == S[3] else "Good")