

num_chars = int(input()) #number of characters
chars = input() #characters

if num_chars % 2 == 1: #if there are an odd number of characters
    print(num_chars) #print the number of characters
    print(chars) #print all the characters
else:
    num_deletions = 0 #number of deletions
    for i in range(0, num_chars-1, 2): #iterate over every pair of characters
        if chars[i] == chars[i+1]: #if the characters are the same
            num_deletions += 1 #add to the number of deletions
    print(num_deletions) #print the number of deletions
    if num_deletions == 0: #if there are no deletions
        print(chars) #print the characters
    else:
        for i in range(0, num_chars-1, 2): #iterate over every pair of characters
            if num_deletions == 0: #if there are no more deletions
                print(chars[i:]) #print the rest of the characters
                break #exit the loop
            if chars[i] == chars[i+1]: #if the characters are the same
                num_deletions -= 1 #subtract from the number of deletions
            else:
                print(chars[i], end='') #print the character
