

#S = input()
S = "akasaka"
#print(S[:int((len(S)-1)/2)])
#print(S[:int((len(S)-1)/2)][::-1])
#print(S[int((len(S)+3)/2)-1:])
#print(S[int((len(S)+3)/2)-1:][::-1])
if S == S[::-1]:
    if S[:int((len(S)-1)/2)] == S[:int((len(S)-1)/2)][::-1]:
        if S[int((len(S)+3)/2)-1:] == S[int((len(S)+3)/2)-1:][::-1]:
            print("Yes")
            exit()
print("No")
