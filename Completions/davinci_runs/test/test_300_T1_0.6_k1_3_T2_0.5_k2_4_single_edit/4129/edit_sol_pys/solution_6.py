import os
import datetime


def create_file(name, text=None):
    with open(name, 'w', encoding='utf-8') as f:
        if text:
            f.write(text)


def create_folder(name):
    try:
        os.mkdir(name)
    except FileExistsError:
        print('Такая папка уже есть')


def get_list(folders_only=False):
    result = os.listdir()
    if folders_only:
        result = [f for f in result if os.path.isdir(f)]
    print(result)


def delete_file(name):
    if os.path.isdir(name):
        os.rmdir(name)
    else:
        os.remove(name)


def copy_file(name, new_name):
    if os.path.isdir(name):
        try:
            os.mkdir(new_name)
        except FileExistsError:
            print('Такая папка уже есть')
    else:
        with open(name, 'r', encoding='utf-8') as f:
            text = f.read()
        with open(new_name, 'w', encoding='utf-8') as f:
            f.write(text)


def save_info(message):
    current_time = datetime.datetime.now()
    result = f'{current_time} - {message}'
    with open('log.txt', 'a', encoding='utf-8') as f:
        f.write(result + '\n')


if __name__ == '__main__':
    create_file('text.dat', 'some text')
    create_file('text.dat')
    create_folder('new_folder')
    get_list()
    get_list(True)
    delete_file('text.dat')
    copy_file('new_folder', 'new_folder_2')
    copy_file('new_file', 'new_file_2')
    save_info('Привет мир')
