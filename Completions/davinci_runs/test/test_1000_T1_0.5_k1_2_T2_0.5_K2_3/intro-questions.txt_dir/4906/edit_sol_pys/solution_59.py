
import sys

def main():
    encode = sys.stdin.readline().strip().split()
    if encode[0] == "E":
        print(encode_func(encode[1]))
    else:
        print(decode_func(encode[1]))

def encode_func(encode):
    encoded = ''
    count = 0
    for i in range(len(encode)):
        count += 1
        if i == len(encode)-1 or encode[i] != encode[i+1]:
            encoded += encode[i] + str(count)
            count = 0
    return encoded

def decode_func(encode):
    decoded = ""
    for i in range(len(encode)):
        if i % 2 == 0:
            decoded += encode[i] * int(encode[i+1])
    return decoded

if __name__ == "__main__":
    main()
