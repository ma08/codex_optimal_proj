# -*- coding: utf-8 -*-

import os
import sys
import json

from collections import defaultdict

class File:

    def __init__(self, filename):
        self.filename = filename
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, 'r')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

    def __iter__(self):
        return self

    def __next__(self):
        line = self.file.readline()
        if not line:
            raise StopIteration
        return line.rstrip('\n')


def read_json(filename):
    with open(filename, 'r') as f:
        return json.loads(f.read())


def write_json(filename, data):
    with open(filename, 'w') as f:
        f.write(json.dumps(data))


def create_file(filename):
    with open(filename, 'w') as f:
        pass


def read_file(filename):
    with open(filename, 'r') as f:
        return f.read()


def write_file(filename, data):
    with open(filename, 'w') as f:
        f.write(data)


def append_file(filename, data):
    with open(filename, 'a') as f:
        f.write(data)


def append_file_ln(filename, data):
    with open(filename, 'a') as f:
        f.write(data + '\n')


def read_file_ln(filename):
    with open(filename, 'r') as f:
        return f.readline().rstrip('\n')


def read_file_lns(filename):
    with open(filename, 'r') as f:
        return f.readlines()


def read_file_lns_stripped(filename):
    with open(filename, 'r') as f:
        return [x.rstrip('\n') for x in f.readlines()]


def read_file_lns_stripped_filter_empty(filename):
    with open(filename, 'r') as f:
        return [x.rstrip('\n') for x in f.readlines() if x.rstrip('\n')]


def read_file_lns_stripped_filter_empty_iter(filename):
    with open(filename, 'r') as f:
        for line in f:
            line = line.rstrip('\n')
            if line:
                yield line


def read_file_lns_stripped_filter_empty_iter_split(filename):
    with open(filename, 'r') as f:
        for line in f:
            line = line.rstrip('\n')
            if line:
                yield line.split()


def read_file_lns_stripped_iter(filename):
    with open(filename, 'r') as f:
        for line in f:
            yield line.rstrip('\n')


def read_file_lns_stripped_iter_split(filename):
    with open(filename, 'r') as f:
        for line in f:
            yield line.rstrip('\n').split()


def read_file_lns_stripped_iter_split_to_dict(filename):
    with open(filename, 'r') as f:
        for line in f:
            yield dict(zip(('key', 'value'), line.rstrip('\n').split()))


def read_file_lns_stripped_iter_split_to_dict_group_by_key(filename):
    result = defaultdict(list)
    with open(filename, 'r') as f:
        for line in f:
            key, value = line.rstrip('\n').split()
            result[key].append(value)
    return result


def read_file_lns_stripped_iter_split_to_dict_group_by_key_sorted_by_key(filename):
    result = read_file_lns_stripped_iter_split_to_dict_group_by_key(filename)
    return sorted(result.items(), key=lambda x: x[0])


def read_file_lns_stripped_iter_split_to_dict_group_by_key_sorted_by_value(filename):
    result = read_file_lns_stripped_iter_split_to_dict_group_by_key(filename)
    return sorted(result.items(), key=lambda x: x[1])


def read_file_lns_stripped_iter_split_to_dict_group_by_key_sorted_by_key_len(filename):
    result = read_file_lns_stripped_iter_split_to_dict_group_by_key(filename)
    return sorted(result.items(), key=lambda x: len(x[0]))


def read_file_lns_stripped_iter_split_to_dict_group_by_key_sorted_by_value_len(filename):
    result = read_file_lns_stripped_iter_split_to_dict_group_by_key(filename)
    return sorted(result.items(), key=lambda x: len(x[1]))


def clear_file(filename):
    with open(filename, 'w') as f:
        pass


def remove_file(filename):
    os.remove(filename)


def get_file_size(filename):
    return os.path.getsize(filename)


def get_file_dir(filename):
    return os.path.dirname(filename)


def get_file_name(filename):
    return os.path.basename(filename)


def get_file_name_without_ext(filename):
    return os.path.splitext(os.path.basename(filename))[0]


def get_file_ext(filename):
    return os.path.splitext(os.path.basename(filename))[1]


def get_file_path(filename):
    return os.path.abspath(filename)


def get_file_path_without_ext(filename):
    return os.path.splitext(os.path.abspath(filename))[0]


def file_exists(filename):
    return os.path.exists(filename)


def file_is_file(filename):
    return os.path.isfile(filename)


def file_is_dir(filename):
    return os.path.isdir(filename)


def file_is_link(filename):
    return os.path.islink(filename)


def file_is_readable(filename):
    return os.access(filename, os.R_OK)


def file_is_writable(filename):
    return os.access(filename, os.W_OK)


def file_is_executable(filename):
    return os.access(filename, os.X_OK)


if __name__ == '__main__':
    pass
