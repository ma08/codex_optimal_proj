from pprint import pprint
import os
import sys


def is_pos_int(x):
    try:
        x = int(x)
        if x > 0:
            return True
        else:
            return False
    except ValueError:
        return False


def is_valid_count(x):
    try:
        x = int(x)
        if 0 <= x <= 10:
            return True
        else:
            return False
    except ValueError:
        return False


def list_file(path):
    try:
        files = os.listdir(path)
        if len(files) == 0:
            return 'Folder is empty'
        else:
            return files
    except FileNotFoundError:
        return 'Folder not found'


def count_files(files):
    count = 0
    for file in files:
        if os.path.isfile(file):
            count += 1
    return count


def count_bytes(files):
    total_bytes = 0
    for file in files:
        if os.path.isfile(file):
            total_bytes += os.path.getsize(file)
    return total_bytes


def get_file_info(file):
    file_info = {}
    file_info['name'] = os.path.basename(file)
    file_info['size'] = os.path.getsize(file)
    file_info['date'] = os.path.getmtime(file)
    return file_info


def get_top_files(files, count):
    top_files = []
    for file in files:
        if os.path.isfile(file):
            top_files.append(get_file_info(file))

    top_files.sort(key=lambda x: x['size'], reverse=True)
    return top_files[:count]


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('No path provided')
        sys.exit()

    path = sys.argv[1]
    files = list_file(path)
    if files == 'Folder is empty':
        print('Folder is empty')
        sys.exit()
    elif files == 'Folder not found':
        print('Folder not found')
        sys.exit()

    print('Total files: ', count_files(files))
    print('Total bytes: ', count_bytes(files))

    if len(sys.argv) > 2:
        count = sys.argv[2]
        if is_valid_count(count):
            top_files = get_top_files(files, int(count))
            pprint(top_files)
        else:
            print('Count must be between 0 and 10')
            sys.exit()

