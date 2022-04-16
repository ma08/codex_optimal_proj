
import sys

def encode(string):
    encoded = ""
    prev, count = string[0], 0
    for c in string:
        if c == prev:
            count += 1
        else:
            encoded += prev + str(count)
            prev = c
            count = 1
    encoded += prev + str(count)  # add last encoded character
    return encoded

def decode(string):
    decoded = ""
    for i in range(0, len(string), 2):  # go through every 2 characters
        decoded += string[i]*int(string[i+1])  # decode the characters
    return decoded

def main():
    line = sys.stdin.readline().strip()
    if line[0] == "E":  # encode
        print(encode(line[2:]))
    else:  # decode
        print(decode(line[2:]))

if __name__ == '__main__':
    main()
