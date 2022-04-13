
import sys

def decode(messages):
    decoded = ""
    for i in range(0,len(messages),2):
        decoded += messages[i]*int(messages[i+1])
    return decoded

def encode(messages):
    encoded = ""
    prev = ""
    count = 0
    for i in range(len(messages)):
        if messages[i] == prev:
            count += 1
        else:
            if prev != "":
                encoded += prev + str(count)
            prev = messages[i]
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
