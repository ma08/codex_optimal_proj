

# number of strings
n = int(input())

# dictionary of letters
letters = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}

for i in range(n):
    # input string
    string = input()
    
    # list of letters in string
    letters_in_string = []
    
    # check if all letters are unique
    for j in range(len(string)):
        if string[j] not in letters_in_string:
            letters_in_string.append(string[j])
        else:
            print("No")
            break
    else:
        # check if letters are consecutive
        for j in range(len(letters_in_string) - 1):
            if letters[letters_in_string[j]] + 1 != letters[letters_in_string[j + 1]]:
                print("No")
                break
        else:
            print("Yes")