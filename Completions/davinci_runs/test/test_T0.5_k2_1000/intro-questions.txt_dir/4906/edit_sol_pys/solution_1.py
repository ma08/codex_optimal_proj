

def main():
    input_list = input().split()
    if input_list[0] == 'E':  # encode
        print(encode(input_list[1]))  # encode the second input
    elif input_list[0] == 'D':  # decode
        print(decode(input_list[1]))  # decode the second input


def encode(text):
    encoded_text = ''  # the encoded text
    cur_char = ''  # the current character
    char_count = 0  # the number of the current character
    for char in text:
        if char == cur_char:  # if the current character is the same as the previous one
            char_count += 1  # increase the number of the current character
        else:  # if the current character is different from the previous one
            if cur_char != '':  # if the previous character is not empty
                encoded_text += cur_char + str(char_count)  # add the previous character and its number to the encoded text
            cur_char = char  # set the current character to the current one
            char_count = 1  # set the number of the current character to 1
    encoded_text += cur_char + str(char_count)  # add the last character and its number to the encoded text
    return encoded_text


def decode(text):
    decoded_text = ''
    for i in range(0, len(text), 2):
        decoded_text += text[i]*int(text[i+1])
    return decoded_text


if __name__ == '__main__':
    main()
