

def main():
    message = input()
    message_length = len(message)
    half_message_length = int(message_length / 2)
    half_message_1 = message[0:half_message_length]
    half_message_2 = message[half_message_length:message_length]

    half_message_1_shift = 0
    half_message_2_shift = 0

    for message_char in half_message_1:
        half_message_1_shift += ord(message_char) - 65
    for message_char in half_message_2:
        half_message_2_shift += ord(message_char) - 65

    half_message_1_shift = half_message_1_shift % 26
    half_message_2_shift = half_message_2_shift % 26

    half_message_1_shifted = ""
    half_message_2_shifted = ""

    for message_char in half_message_1:
        half_message_1_shifted += chr((ord(message_char) - 65 + half_message_1_shift) % 26 + 65)
    for message_char in half_message_2:
        half_message_2_shifted += chr((ord(message_char) - 65 + half_message_2_shift) % 26 + 65)

    decrypted_message = ""

    for i in range(half_message_length):
        decrypted_message += chr((ord(half_message_1_shifted[i]) - 65 + ord(half_message_2_shifted[i]) - 65) % 26 + 65)

    print(decrypted_message)

if __name__ == '__main__':
    main()
