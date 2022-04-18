

import sys

def main():
    passwords = [] # list of passwords and their probabilities
    for line in sys.stdin:
        passwords.append(line.strip().split()) # split line into password and probability
    passwords = [[int(p), float(prob)] for p, prob in passwords] # convert to int and float
    passwords.sort(key=lambda x: x[1], reverse=True) # sort in descending order of probabilities
    expected = 0
    for i, p in enumerate(passwords):
        expected += (i + 1) * p[1]
    print(expected)

if __name__ == "__main__":
    main()
