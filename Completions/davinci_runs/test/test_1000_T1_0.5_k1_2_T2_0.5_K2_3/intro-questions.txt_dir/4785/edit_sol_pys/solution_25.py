

s = input() # takes input
for i in range(len(s)-1): # checks each character
    if s[i] == 's' and s[i+1] == 's': # checks if the character is 's' and the next character is also 's'
        print('hiss')
        break
else:
    print('no hiss') 
