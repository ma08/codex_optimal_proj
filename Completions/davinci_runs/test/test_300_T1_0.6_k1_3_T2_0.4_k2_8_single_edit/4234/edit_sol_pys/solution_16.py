

num_chars = int(input())  # number of characters in the input string
chars = input()  # input string

if num_chars % 2 == 0:
    # if the number of characters is even, we can remove only pairs of the same character
    # the number of pairs of the same character is the number of deletions we need to make
    num_deletions = 0
    for i in range(0, num_chars-1, 2):
        if chars[i] == chars[i+1]:

    # print the number of deletions and the string with the deletions
            num_deletions += 1

    # if there are no deletions, we just print the string
    print(num_deletions)
    if num_deletions == 0:
        print(chars)
        # otherwise, we print the string with the deletions
    else:
        for i in range(0, num_chars-1, 2):
            if num_deletions == 0:
                print(chars[i:])
                break
            if chars[i] == chars[i+1]:
                num_deletions -= 1
            else:
                print(chars[i], end='')
else:
    # if the number of characters is odd, we can't make any deletions
    # so we print the number of characters and the string
    print(num_chars)
    print(chars)
