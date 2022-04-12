

word = input("Enter a word: ")

# find the number of unique letters in the word
unique_letters = set(word)

# if there is only one letter, we are done
if len(unique_letters) == 1:
    print("The shortest substring that is repeated at least twice is: " + word[0])
    exit()

# otherwise, we need to find the smallest length of a substring that is repeated
# at least twice in the word

# we will try all possible lengths of substrings 
# we start with the smallest length, which is 2

length = 2

# we will keep searching for the substring until we find one that is repeated
# at least twice

while True:

    # we will need to keep track of the substrings we have seen
    # we will do this by storing a dictionary
    # the dictionary will have the substring as the key,
    # and the number of times it appears in the word as the value
    # for example, if we have the word abcabc, and we are currently
    # looking for substrings of length 2, we will have the dictionary
    # {'ab': 2, 'bc': 2, 'ca': 1}

    # we start off with an empty dictionary
    substrings = {}

    # now, we will go through all substrings of length length
    # we will start at the beginning of the word
    # we will stop when we get to the end of the word
    # we will increment by one each time
    for start in range(len(word) - length + 1):

        # we get the substring
        substring = word[start:start + length]

        # if the substring is not in the dictionary, we add it
        if substring not in substrings:
            substrings[substring] = 0

        # we increment the number of times the substring appears in the word
        substrings[substring] += 1

    # we will check if any substrings appear at least twice
    for substring in substrings:
        if substrings[substring] >= 2:
            # if so, we are done
            print("The shortest substring that is repeated at least twice is: " + substring)
            exit()

    # if we didn't find any substrings that appear at least twice,
    # we increase the length of the substring and try again
    length += 1
