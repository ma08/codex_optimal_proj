

import sys

def main():
    # get input
    _input = sys.stdin.readlines()
    _input = [x.strip() for x in _input]

    # find out if encoding or decoding
    if _input[0][0] == 'E':
        encoded = encode(_input[0][2:])
        print(encoded)
    else:
        decoded = decode(_input[0][2:])
        print(decoded)

def encode(string):
    encoded = ''
    count = 1
    for i in range(len(string) - 1): # loop through all but last character
        if string[i] == string[i+1]:
            count += 1
        else:
            encoded += string[i] + str(count)
            count = 1
    encoded += string[-1] + str(count) # add last character
    return encoded

def decode(string):
    decoded = ''
    for i in range(0, len(string), 2): # loop through every other character
        decoded += string[i] * int(string[i+1])
    return decoded

if __name__ == '__main__':
    main()
