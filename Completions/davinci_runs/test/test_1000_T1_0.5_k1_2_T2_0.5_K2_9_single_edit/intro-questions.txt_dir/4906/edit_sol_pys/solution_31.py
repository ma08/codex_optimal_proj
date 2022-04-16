
import sys

def main():
    for line in sys.stdin:
        encoding = line.strip().split()
        if encoding[0] == "E":
            print(encode(encoding[1]))
        else:
            print(decode(encoding[1]))

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
