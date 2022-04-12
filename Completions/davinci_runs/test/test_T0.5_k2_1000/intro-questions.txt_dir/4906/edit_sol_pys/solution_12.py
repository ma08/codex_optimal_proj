import sys

def encode(string):
    encoded = ""
    prev = string[0]
    count = 0
    for c in string:
        if c == prev:
            count += 1
        else:
            encoded += prev + str(count)
            prev = c
            count = 1
    encoded += prev + str(count)
    return encoded

def decode(string):
    decoded = ""
    for i in range(0, len(string), 2):
        decoded += string[i]*int(string[i+1])
    return decoded

def main():
    line = sys.stdin.readline().strip()
    if line[0] == "E":
        print(encode(line[2:]))
    else:
        print(decode(line[2:]))

if __name__ == '__main__':
    main()
