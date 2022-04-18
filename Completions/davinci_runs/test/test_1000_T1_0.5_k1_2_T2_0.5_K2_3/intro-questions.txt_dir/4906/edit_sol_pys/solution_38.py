
import sys

def main():
    encoded = sys.stdin.readline().strip().split()
    print(encode(encoded[1]))
    print(decode(encoded[1]))

def encode(string):
    encoded = ""
    count = 0
    for i in range(len(string)):
        count += 1
        if i == len(string)-1 or string[i] != string[i+1]:
            encoded += string[i] + str(count)
            count = 0
    return encoded

def decode(string):
    decoded = ""
    for i in range(len(string)):
        if i % 2 == 0:
            decoded += string[i] * int(string[i+1])
    return decoded

if __name__ == "__main__":
    main()
