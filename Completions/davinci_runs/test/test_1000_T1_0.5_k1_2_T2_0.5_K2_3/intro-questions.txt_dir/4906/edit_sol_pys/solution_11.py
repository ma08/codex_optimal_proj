

def main():
    input_list = input().split()
    if input_list[0] == 'E' or input_list[0] == 'e':
        print(encode(input_list[1]))
    elif input_list[0] == 'D' or input_list[0] == 'd':
        print(decode(input_list[1]))


def encode(text):
    encoded_text = ''
    cur_char = ''
    char_count = 0
    for char in text:
        if char == cur_char:
            char_count += 1
        else:
            if cur_char != '':
                encoded_text += cur_char + str(char_count)
            cur_char = char
            char_count = 1
    encoded_text += cur_char + str(char_count)
    return encoded_text


def decode(text):
    decoded_text = ''
    for i in range(0, len(text), 2):
        decoded_text += text[i] * int(text[i+1])
    return decoded_text


if __name__ == '__main__':
    main()
