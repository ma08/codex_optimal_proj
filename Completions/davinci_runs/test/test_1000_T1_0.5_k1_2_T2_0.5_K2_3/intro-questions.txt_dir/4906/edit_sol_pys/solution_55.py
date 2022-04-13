

import sys

def main():
    encode_decode = sys.stdin.readline().strip().split()
    if encode_decode[0] == "E":
        print(encode(encode_decode[1]))
    else:
        print(decode(encode_decode[1]))

def encode(encode):
    encoded = ''
    count = 0
    for i in range(len(encode)):
        count += 1
        if i == len(encode)-1 or encode[i] != encode[i+1]:
            encoded += encode[i] + str(count)
            count = 0
    return encoded

def decode(encode):
    decoded = ""
    for i in range(len(encode)):
        if i % 2 == 0:
            decoded += encode[i] * int(encode[i+1])
    return decoded

if __name__ == "__main__":
    main()
