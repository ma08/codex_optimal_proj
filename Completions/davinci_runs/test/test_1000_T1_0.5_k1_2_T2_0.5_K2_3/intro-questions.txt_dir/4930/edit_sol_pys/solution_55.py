
text = input('Enter text: ')


def decode(text: str) -> str:
    decoded = ''
    for i in range(len(text) - 1):
        if text[i] not in 'aeiou':
            decoded += text[i]
    return decoded + text[-1]

print(f'Decoded text: {decode(text)}')  # Decoded text: bbbbcccdddd
