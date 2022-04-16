

import sys

def main():
    line = sys.stdin.readline().strip().split()
    if line[0] == "E":
        encode(line[1])
    elif line[0] == "D":
        decode(line[1])

def encode(string):
    encoded_string = ""
    count = 1
    for i in range(1, len(string)):
        if string[i] == string[i-1]:
            count += 1
        else:
            encoded_string += string[i-1] + str(count)
            count = 1
    encoded_string += string[-1] + str(count)
    print(encoded_string)

def decode(string):
    decoded_string = ""
    for i in range(0, len(string), 2):
        decoded_string += string[i] * int(string[i+1])
    print(decoded_string)

if __name__ == "__main__":
    main()
