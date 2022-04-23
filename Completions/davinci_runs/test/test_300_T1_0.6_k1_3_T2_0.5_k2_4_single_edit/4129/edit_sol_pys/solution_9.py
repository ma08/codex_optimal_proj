#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

# Проверяем аргументы командной строки
if len(sys.argv) != 2:
    print("Использование: file.py <путь к каталогу>")
    sys.exit(1)

# Получаем аргумент командной строки
dir_path = sys.argv[1]

# Проверяем, является ли аргумент командной строки каталогом
if not os.path.isdir(dir_path):
    print("Данный путь не является каталогом")
    sys.exit(1)

# Получаем список файлов в каталоге
files = os.listdir(dir_path)

# Пробегаемся по списку файлов в каталоге
for file in files:
    # Получаем полный путь к файлу
    file_path = os.path.join(dir_path, file)
    # Проверяем, является ли файл каталогом
    if os.path.isdir(file_path):
        # Если файл является каталогом, пропускаем его
        continue
    # Получаем информацию о файле
    file_info = os.stat(file_path)
    # Получаем информацию о размере файла
    file_size = file_info.st_size
    # Выводим информацию о файле
    print("Файл: %s, размер: %d байт" % (file, file_size))
