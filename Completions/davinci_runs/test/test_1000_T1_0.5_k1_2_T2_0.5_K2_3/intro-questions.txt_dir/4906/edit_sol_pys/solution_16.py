
import sys, string

def decode(message, ignore_case):
    decoded = ""
    i = 0
    while i < len(message):
        if message[i].isalpha():
            if ignore_case:
                decoded += message[i].lower()*int(message[i+1])
            else:
                decoded += message[i]*int(message[i+1])
            i += 2
        else:
            decoded += message[i]
            i += 1
    return decoded

def encode(message, ignore_case):
    encoded = ""
    prev = ""
    count = 0
    i = 0
    while i < len(message):
        if message[i].isalpha():
            if ignore_case:
                if message[i].lower() == prev:
                    count += 1
                else:
                    if prev != "":
                        encoded += prev + str(count)
                    prev = message[i].lower()
                    count = 1
            else:
                if message[i] == prev:
                    count += 1
                else:
                    if prev != "":
                        encoded += prev + str(count)
                    prev = message[i]
                    count = 1
            i += 1
        else:
            encoded += message[i]
            i += 1
    encoded += prev + str(count)
    return encoded

def main():
    line = sys.stdin.readline().strip().split(" ")
    if line[0] == "E":
        print(encode(line[1], line[2] == "T"))
    else:
        print(decode(line[1], line[2] == "T"))

main()
