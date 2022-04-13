
S = input() #input string
count = 0   #initialize count

for i in range(len(S)-1):  #loop through the string
    if S[i] == S[i+1]:  #check if the letter is equal to the next letter
        count += 1

print(count)
