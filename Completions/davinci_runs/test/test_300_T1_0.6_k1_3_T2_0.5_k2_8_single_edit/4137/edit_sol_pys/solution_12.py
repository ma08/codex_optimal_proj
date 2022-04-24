
import logging

logging.basicConfig(level=logging.INFO)


def get_lines(file_name):
    with open(file_name) as file:
        return file.readlines()


def get_data(file_name):
    lines = get_lines(file_name)
    data = []
    for line in lines:
        line = line.strip()
        if line:
            data.append(line)
    return data


def get_files(file_name):
    return get_data(file_name)


def get_file_content(file_name):
    return get_data(file_name)


def get_file_lines(file_name):
    return get_lines(file_name)


def get_file_line(file_name):
    lines = get_file_lines(file_name)
    return lines[0]


def write_file(file_name, lines):
    with open(file_name, "w") as file:
        file.writelines(lines)


def write_file_content(file_name, content):
    lines = []
    for item in content:
        lines.append(item + "\n")
    write_file(file_name, lines)


def write_file_line(file_name, line):
    write_file_content(file_name, [line])


def append_file(file_name, lines):
    with open(file_name, "a") as file:
        file.writelines(lines)


def append_file_content(file_name, content):
    lines = []
    for item in content:
        lines.append(item + "\n")
    append_file(file_name, lines)


def append_file_line(file_name, line):
    append_file_content(file_name, [line])


def remove_file(file_name):
    import os
    os.remove(file_name)


def get_file_size(file_name):
    import os
    return os.path.getsize(file_name)


def get_file_size_str(file_name):
    size = get_file_size(file_name)
    if size < 1024:
        return str(size) + "B"
    if size < 1024 * 1024:
        return str(round(size / 1024, 2)) + "KB"
    if size < 1024 * 1024 * 1024:
        return str(round(size / (1024 * 1024), 2)) + "MB"
    if size < 1024 * 1024 * 1024 * 1024:
        return str(round(size / (1024 * 1024 * 1024), 2)) + "GB"
    return str(round(size / (1024 * 1024 * 1024 * 1024), 2)) + "TB"


def get_file_extension(file_name):
    import os
    return os.path.splitext(file_name)[1]


def get_file_name(file_name):
    import os
    return os.path.splitext(os.path.basename(file_name))[0]


def get_file_path(file_name):
    import os
    return os.path.dirname(file_name)


def get_file_path_name(file_name):
    import os
    return os.path.basename(file_name)


def get_file_path_name_extension(file_name):
    import os
    return os.path.basename(file_name)


def get_file_path_name_without_extension(file_name):
    import os
    return os.path.splitext(os.path.basename(file_name))[0]


def get_file_path_without_name(file_name):
    import os
    return os.path.dirname(file_name)


def get_file_path_without_name_extension(file_name):
    import os
    return os.path.dirname(file_name)


def get_file_path_without_name_without_extension(file_name):
    import os
    return os.path.dirname(file_name)


def get_file_path_without_extension(file_name):
    import os
    return os.path.splitext(file_name)[0]


def get_file_path_extension(file_name):
    import os
    return os.path.splitext(file_name)[1]


def is_file_exists(file_name):
    import os
    return os.path.exists(file_name)


def is_file_not_exists(file_name):
    return not is_file_exists(file_name)


def is_file_empty(file_name):
    return is_file_size_zero(file_name)


def is_file_not_empty(file_name):
    return is_file_size_not_zero(file_name)


def is_file_size_zero(file_name):
    return get_file_size(file_name) == 0


def is_file_size_not_zero(file_name):
    return get_file_size(file_name) != 0


def is_file_size_less_than(file_name, size):
    return get_file_size(file_name) < size


def is_file_size_less_than_or_equal(file_name, size):
    return get_file_size(file_name) <= size


def is_file_size_greater_than(file_name, size):
    return get_file_size(file_name) > size


def is_file_size_greater_than_or_equal(file_name, size):
    return get_file_size(file_name) >= size


if __name__ == "__main__":
    file_name = "file.py"
    print(get_file_size(file_name))
    print(get_file_size_str(file_name))
    print(get_file_extension(file_name))
    print(get_file_name(file_name))
    print(get_file_path(file_name))
    print(get_file_path_name(file_name))
    print(get_file_path_name_extension(file_name))
    print(get_file_path_name_without_extension(file_name))
    print(get_file_path_without_name(file_name))
    print(get_file_path_without_name_extension(file_name))
    print(get_file_path_without_name_without_extension(file_name))
    print(get_file_path_without_extension(file_name))
    print(get_file_path_extension(file_name))
    print(is_file_exists(file_name))
    print(is_file_not_exists(file_name))
    print(is_file_empty(file_name))
    print(is_file_not_empty(file_name))
    print(is_file_size_zero(file_name))
    print(is_file_size_not_zero(file_name))
    print(is_file_size_less_than(file_name, 0))
    print(is_file_size_less_than
