
import sys

    string_to_encode = string_to_encode.strip()
def encode(string_to_encode):
    encoded_string = ""
    count = 1
    for i in range(len(string_to_encode) - 1):
        if string_to_encode[i] == string_to_encode[i + 1]:
            count += 1
        else:
            encoded_string += string_to_encode[i] + str(count)
            count = 1
    encoded_string += string_to_encode[-1]
    if count > 1:
        encoded_string += str(count)
    return encoded_string

    string_to_decode = string_to_decode.strip()
def decode(string_to_decode):
    decoded_string = ""
    for i in range(0, len(string_to_decode) - 1, 2):
        decoded_string += string_to_decode[i] * int(string_to_decode[i + 1])
    return decoded_string

def main():
    for line in sys.stdin:
        if line[0] == "E" or line[0] == "e":
            print(encode(line[2:].strip()))
        else:
            print(decode(line[2:].strip()))

if __name__ == '__main__':
    main()
