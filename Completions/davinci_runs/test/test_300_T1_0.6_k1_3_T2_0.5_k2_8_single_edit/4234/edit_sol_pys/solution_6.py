

num_chars = int(input()) # get number of characters
chars = input() # get characters

if num_chars % 2 == 1: # if number of characters is odd
    print(num_chars)
    print(chars)
else: # if number of characters is even
    num_deletions = 0
    for i in range(0, num_chars-1, 2): # iterate through every 2 characters
        if chars[i] == chars[i+1]: # if the 2 characters are the same
            num_deletions += 1
    print(num_deletions)
    if num_deletions == 0: # if there were no deletions
        print(chars)
    else: # if there were deletions
        for i in range(0, num_chars-1, 2):
            if num_deletions == 0: # if we have deleted all the necessary characters
                print(chars[i:])
                break
            if chars[i] == chars[i+1]: # if the 2 characters are the same
                num_deletions -= 1
            else:
                print(chars[i], end='')
