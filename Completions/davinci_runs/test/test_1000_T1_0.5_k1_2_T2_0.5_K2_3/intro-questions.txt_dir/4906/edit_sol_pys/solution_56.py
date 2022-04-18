
def encode(text):
    encoded_text = ''
    cur_symbol = ''
    symbol_count = 0
    for char in text:
        if char == cur_symbol:
            symbol_count += 1
        else:
            if cur_symbol != '':
                encoded_text += str(symbol_count) + cur_symbol
            cur_symbol = char
            symbol_count = 1
    encoded_text += str(symbol_count) + cur_symbol
    return encoded_text


def decode(text):
    decoded_text = ''
    for i in range(0, len(text), 2):
        decoded_text += text[i+1]*int(text[i])
    return decoded_text


if __name__ == '__main__':
    input_list = input().split()
    if input_list[0] == 'E':
        print(encode(input_list[1]))
    elif input_list[0] == 'D':
        print(decode(input_list[1]))
