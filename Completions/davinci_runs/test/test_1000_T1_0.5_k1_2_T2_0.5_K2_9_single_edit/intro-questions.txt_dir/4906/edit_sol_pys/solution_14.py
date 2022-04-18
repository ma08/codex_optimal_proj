#!/usr/bin/env python3

import sys

def encode(msg):
    msg = list(msg)
    new_msg = ""
    count = 1
    for i in range(len(msg)):
        if i == len(msg) - 1:
            new_msg += msg[i] + str(count)
            break
        elif msg[i] == msg[i + 1]:
            count += 1
        else:
            new_msg += msg[i] + str(count)
            count = 1
    return new_msg

def decode(msg):
    msg = list(msg)
    new_msg = ""
    count = ""
    for i in range(len(msg)):
        if i % 2 == 0:
            new_msg += msg[i]
        else:
            count += msg[i]
            if i == len(msg) - 1 or msg[i + 1] in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_!.":
                new_msg += msg[i - 1] * int(count)
                count = ""
    return new_msg

def main():
    msg = sys.stdin.readline().strip().split()
    if msg[0] == "E":
        print(encode(msg[1]))
    else:
        print(decode(msg[1]))

if __name__ == '__main__':
    main()
