
import sys

def main():
    # get input
    user_input = sys.stdin.readlines()
    user_input = [x.strip() for x in user_input]

    # find out if encoding or decoding
    if user_input[0][0] == 'E':
        encoded = encode(user_input[0][2:])
        print(encoded)
    else:
        decoded = decode(user_input[0][2:])
        print(decoded)

def encode(string):
    encoded = ''
    count = 1
    for i in range(len(string) - 1):
        if string[i] == string[i+1]:
            count += 1
        else:
            encoded += string[i] + str(count)
            count = 1
    encoded += string[-1] + str(count)
    return encoded

def decode(string):
    decoded = ''
    for i in range(0, len(string), 2):
        decoded += string[i] * int(string[i+1])
    return decoded

if __name__ == '__main__':
    main()
