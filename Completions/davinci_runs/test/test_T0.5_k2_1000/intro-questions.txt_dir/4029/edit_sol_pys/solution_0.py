import os
import sys

def get_file_name():
    if len(sys.argv) < 2:
        print("No file name given")
        sys.exit(1)
    else:
        return sys.argv[1]

def read_file(file_name):
    try:
        with open(file_name, 'r') as f:
            return f.read()
    except FileNotFoundError:
        print("File not found")
        sys.exit(1)

def write_file(file_name, content):
    with open(file_name, 'w') as f:
        f.write(content)

def get_file_content(file_name):
    return read_file(file_name)

def get_file_content_with_prompt(file_name):
    content = input("Enter file content: ")
    return content

def get_file_content_with_prompt_and_default(file_name):
    content = input("Enter file content (default is file content): ")
    if content == "":
        return get_file_content(file_name)
    else:
        return content

def get_file_content_with_prompt_and_default_and_append(file_name):
    content = input("Enter file content (default is file content): ")
    if content == "":
        return get_file_content(file_name) + "\n" + content
    else:
        return content

def get_file_content_with_prompt_and_append(file_name):
    content = input("Enter file content: ")
    return get_file_content(file_name) + "\n" + content

def main():
    file_name = get_file_name()
    content = get_file_content_with_prompt_and_default_and_append(file_name)
    write_file(file_name, content)

if __name__ == '__main__':
    main()
