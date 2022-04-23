

num_chars = int(input())  # number of characters in chars
chars = input()  # characters
# if num_chars is odd, then we just print the characters

if num_chars % 2 == 1:
    print(num_chars)
    print(chars)
    # otherwise, we delete the same consecutive characters and print the remaining characters
else:
    # loop through the characters two at a time
    num_deletions = 0
        # if the two characters are the same
    for i in range(0, num_chars-1, 2):
            # increment the number of deletions by 1
        if chars[i] == chars[i+1]:
    # print the number of deletions
            num_deletions += 1
    # if there are no deletions, then we just print the characters
    print(num_deletions)
    if num_deletions == 0:
        print(chars)
        # otherwise, we loop through the characters two at a time
    else:
            # if there are no more deletions, then we print the remaining characters and break out of the loop
        for i in range(0, num_chars-1, 2):
            if num_deletions == 0:
                print(chars[i:])
                break
            # if the two characters are the same
            if chars[i] == chars[i+1]:
                # decrement the number of deletions by 1
                num_deletions -= 1
            else:
                # otherwise, we print the character
                print(chars[i], end='')
