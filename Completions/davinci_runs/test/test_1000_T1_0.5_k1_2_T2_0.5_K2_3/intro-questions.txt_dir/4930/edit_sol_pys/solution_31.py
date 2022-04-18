
text = input('Enter text: ')

def decode(text: str) -> str:
    decoded = ''
    for i in range(len(text) - 1):
        if text[i] in 'aeiou' and text[i + 1] in 'aeiou':
            continue        
        decoded += text[i]
    decoded += text[-1]
    return decoded 

print(f'Decoded text: {decode(text)}')
