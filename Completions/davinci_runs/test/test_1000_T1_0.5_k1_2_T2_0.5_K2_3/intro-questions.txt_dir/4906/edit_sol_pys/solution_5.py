
import sys

def encode(string_to_encode):
    encoded_string = ""
    count = 1
    for i in range(len(string_to_encode)-1):
        if string_to_encode[i] == string_to_encode[i+1]:
            count += 1
        else:
            encoded_string += string_to_encode[i] + str(count)
            count = 1
    encoded_string += string_to_encode[-1] + str(count)
    return encoded_string

def decode(string_to_decode):
    decoded_string = ""
    for i in range(0, len(string_to_decode)-1, 2):
        decoded_string += string_to_decode[i] * int(string_to_decode[i+1])
    return decoded_string

def main():
    for line in sys.stdin:
        if line[0] == "E":
            print(encode(line[2:]))
        else:
            print(decode(line[2:]))

if __name__ == '__main__':
    main()
