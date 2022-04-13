
def decrypt(message):
    half_message_length = int(len(message) / 2)
    half_message_1 = message[0:half_message_length]  # first half of message
    half_message_2 = message[half_message_length:len(message)]  # second half of message
    half_message_1_rotation = 0
    half_message_2_rotation = 0
    for message_char in half_message_1:
        half_message_1_rotation += ord(message_char) - 65
    for message_char in half_message_2:
        half_message_2_rotation += ord(message_char) - 65
    half_message_1_rotation = half_message_1_rotation % 26
    half_message_2_rotation = half_message_2_rotation % 26
    half_message_1_rotate = ""
    half_message_2_rotate = ""
    for message_char in half_message_1:
        half_message_1_rotate += chr((ord(message_char) - 65 + half_message_1_rotation) % 26 + 65)
    for message_char in half_message_2:
        half_message_2_rotate += chr((ord(message_char) - 65 + half_message_2_rotation) % 26 + 65)

    decrypted_message = ""

    for i in range(half_message_length):
        decrypted_message += chr((ord(half_message_1_rotate[i]) - 65 + ord(half_message_2_rotate[i]) - 65) % 26 + 65)
    return decrypted_message
