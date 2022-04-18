

import os
import sys

def create_file(file_name, file_path):
    file_name = file_name + '.txt'
    file_path = os.path.join(file_path, file_name)
    f = open(file_path, 'w')
    f.close()

def create_folder(folder_name, folder_path):
    folder_path = os.path.join(folder_path, folder_name)
    os.mkdir(folder_path)

def create(name, path, type):
    if type == 'file':
        create_file(name, path)
    else:
        create_folder(name, path)

def delete_file(file_name, file_path):
    file_name = file_name + '.txt'
    file_path = os.path.join(file_path, file_name)
    os.remove(file_path)

def delete_folder(folder_name, folder_path):
    folder_path = os.path.join(folder_path, folder_name)
    os.rmdir(folder_path)

def delete(name, path, type):
    if type == 'file':
        delete_file(name, path)
    else:
        delete_folder(name, path)

def rename_file(file_name, file_path, new_name):
    file_name = file_name + '.txt'
    file_path = os.path.join(file_path, file_name)
    new_name = new_name + '.txt'
    new_path = os.path.join(os.path.dirname(file_path), new_name)
    os.rename(file_path, new_path)

def rename_folder(folder_name, folder_path, new_name):
    folder_path = os.path.join(folder_path, folder_name)
    new_path = os.path.join(os.path.dirname(folder_path), new_name)
    os.rename(folder_path, new_path)

def rename(name, path, type, new_name):
    if type == 'file':
        rename_file(name, path, new_name)
    else:
        rename_folder(name, path, new_name)

def copy_file(file_name, file_path, new_path):
    file_name = file_name + '.txt'
    file_path = os.path.join(file_path, file_name)
    new_path = os.path.join(new_path, file_name)
    f = open(file_path, 'r')
    content = f.read()
    f.close()
    f = open(new_path, 'w')
    f.write(content)
    f.close()

def copy_folder(folder_name, folder_path, new_path):
    folder_path = os.path.join(folder_path, folder_name)
    new_path = os.path.join(new_path, folder_name)
    os.mkdir(new_path)
    for file in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, file)):
            copy_file(file, folder_path, new_path)
        else:
            copy_folder(file, folder_path, new_path)

def copy(name, path, new_path, type):
    if type == 'file':
        copy_file(name, path, new_path)
    else:
        copy_folder(name, path, new_path)

def move_file(file_name, file_path, new_path):
    file_name = file_name + '.txt'
    file_path = os.path.join(file_path, file_name)
    new_path = os.path.join(new_path, file_name)
    os.rename(file_path, new_path)

def move_folder(folder_name, folder_path, new_path):
    folder_path = os.path.join(folder_path, folder_name)
    new_path = os.path.join(new_path, folder_name)
    os.rename(folder_path, new_path)

def move(name, path, new_path, type):
    if type == 'file':
        move_file(name, path, new_path)
    else:
        move_folder(name, path, new_path)

def print_files(path):
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            print(file)

def print_folders(path):
    for folder in os.listdir(path):
        if os.path.isdir(os.path.join(path, folder)):
            print(folder)

def print_content(path):
    print_folders(path)
    print_files(path)

def print_content_recursive(path):
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            print(file)
        else:
            print(file)
            print_content_recursive(os.path.join(path, file))

def main():
    path = os.getcwd()
    while True:
        print('Текущая папка: ', path)
        print('Выберите действие:')
        print('1 - Создать папку')
        print('2 - Создать файл')
        print('3 - Удалить файл или папку')
        print('4 - Переименовать файл или папку')
        print('5 - Копировать файл или папку')
        print('6 - Переместить файл или папку')
        print('7 - Вывести содержимое текущей папки')
        print('8 - Вывести содержимое текущей папки рекурсивно')
        print('9 - Перейти в папку')
        print('10 - Прекратить работу')
        choice = int(input())
        if choice == 1:
            name = input('Введите
