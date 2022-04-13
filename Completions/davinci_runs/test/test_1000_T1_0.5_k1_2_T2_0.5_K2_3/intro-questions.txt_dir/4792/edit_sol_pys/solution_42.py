import os

def write_to_file(text, file_name):
    if os.path.exists(file_name):
        with open(file_name, 'w') as f:
            f.write(text)
    else:
        with open(file_name, 'w') as f:
            f.write(text)


def read_from_file(file_name):
    if os.path.exists(file_name):
        with open(file_name, 'r') as f:
            return f.read()
    else:
        return None





text = input()
for i in range(1,len(text)):
    if text[i] == text[i-1]:
        text = text[:i] + text[i+1:]
        i -= 1

print(text)
