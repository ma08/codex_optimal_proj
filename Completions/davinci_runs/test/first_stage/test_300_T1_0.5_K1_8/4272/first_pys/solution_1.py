

#S = input().strip()
S = "ZABCDBABCQ"

count = 0
for i in range(len(S)-2):
    if S[i] == "A" and S[i+1] == "B" and S[i+2] == "C":
        count += 1

print(count)