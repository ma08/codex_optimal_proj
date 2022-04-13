

import sys

def main():
    passwords = [] # list of passwords
    for line in sys.stdin:
        passwords.append(line.strip().split()) # get a list of passwords
    passwords = [[int(p), float(prob)] for p, prob in passwords] # convert to int and float
    passwords.sort(key=lambda x: x[1], reverse=True) # sort by probability in descending order
    expected = 0
    for i in range(len(passwords)):
        expected += (i + 1) * passwords[i][1] # i + 1 is the number of guesses
                                              # passwords[i][1] is the probability of that password
    print(expected)

if __name__ == "__main__":
    main()
