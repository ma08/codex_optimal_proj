

import os

def get_files_in_dir(dir_path):
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            yield os.path.join(root, file)


def is_valid_file(file_path):
    return os.path.isfile(file_path) and file_path.endswith('.txt')


def is_valid_dir(dir_path):
    return os.path.isdir(dir_path)


def get_file_content(file_path):
    with open(file_path, 'r') as f:
        return f.read()


def get_dir_content(dir_path):
    content = ''
    for file in get_files_in_dir(dir_path):
        if is_valid_file(file):
            content += get_file_content(file)
    return content


def get_content(path):
    if is_valid_file(path):
        return get_file_content(path)
    elif is_valid_dir(path):
        return get_dir_content(path)
    else:
        return ''


def get_word_count(content):
    return content.split()


def get_sentence_count(content):
    return content.split('.')


def get_character_count(content):
    return content.replace(' ', '')


def get_paragraph_count(content):
    return content.split('\n')


def get_statistics(path):
    content = get_content(path)
    return {
        'word': len(get_word_count(content)),
        'sentence': len(get_sentence_count(content)),
        'character': len(get_character_count(content)),
        'paragraph': len(get_paragraph_count(content))
    }

import re

if __name__ == '__main__':
    path = input('Enter path to file or directory: ')
    print(get_statistics(path))

