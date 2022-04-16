import sys



def main():
    if len(sys.argv) == 4:
        input_file = open(sys.argv[1], 'r')
        output_file = open(sys.argv[2], 'w')
        input_list = input_file.readline().split()
        if input_list[0] == 'E':
            output_file.write(encode(input_list[1]))
        elif input_list[0] == 'D':
            output_file.write(decode(input_list[1]))
        input_file.close()
        output_file.close()
    else:
        print('Invalid arguments')


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
        decoded_text += text[i]*int(text[i+1])
    return decoded_text


if __name__ == '__main__':
    main()
