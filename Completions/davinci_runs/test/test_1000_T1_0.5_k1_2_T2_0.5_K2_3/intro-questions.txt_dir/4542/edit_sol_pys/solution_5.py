

S = input() #input string; same as raw_input() in python 2
count = 0   #initialize count

for i in range(len(S)-1):  #loop through the string
    if S[i] == S[i+1]:
        count += 1

print(count)
