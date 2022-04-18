

import sys


def decode(message):
    decoded = ""
    for i in range(0,len(message),2):
        decoded += message[i]*int(message[i+1])
    return decoded

def encode(message):
    encoded = ""
    prev = ""
    count = 0
    for i in range(len(message)):
        if message[i] == prev:
            count += 1
        else:
            if prev != "":
                encoded += prev + str(count)
            prev = message[i]
            count = 1
    encoded += prev + str(count)
    return encoded

def main():
    line = sys.stdin.readline().strip().split()
    if line[0] == "E":
        print(encode(line[1]))
    else:
        print(decode(line[1]))

main()
