
import sys

def main():
    user_input = sys.stdin.readline().strip().split()
    if user_input[0] == "E":
        encode(user_input[1])
    elif user_input[0] == "D":
        decode(user_input[1])

def encode(string):
    encoded_string = ""
    count = 1
    for i in range(1, len(string)):
        if string[i] == string[i - 1]:
            count += 1
        else:
            encoded_string += string[i - 1] + str(count)
            count = 1
    encoded_string += string[-1] + str(count) # last character
    print(encoded_string)

def decode(string):
    decoded_string = ""
    for i in range(0, len(string), 2):
        decoded_string += string[i] * int(string[i+1])
    print(decoded_string)

if __name__ == "__main__":
    main()
