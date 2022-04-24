import os

def create_file(filename):
    with open(filename, "w") as file:
        file.write("")

def add_to_file(filename, line):
    with open(filename, "a") as file:
        file.write(line)

def get_file_lines():
    with open(filename, "r") as file:
        return file.readlines()

def get_file_content(filename):
    with open(filename, "r") as file:
        return file.read()

def get_file_content_as_list(filename):
    with open(filename, "r") as file:
        return file.read().splitlines()

def get_file_content_as_list_of_lists(filename, delimiter):
    with open(filename, "r") as file:
        return [x.split(delimiter) for x in file.read().splitlines()]

def get_file_content_as_list_of_dicts(filename, delimiter):
    with open(filename, "r") as file:
        lines = file.read().splitlines()
        headers = lines[0].split(delimiter)
        return [dict(zip(headers, x.split(delimiter))) for x in lines[1:]]

def get_file_content_as_dict_of_lists(filename, delimiter):
    with open(filename, "r") as file:
        lines = file.read().splitlines()
        headers = lines[0].split(delimiter)
        return dict(zip(headers, zip(*[x.split(delimiter) for x in lines[1:]])))

def get_file_content_as_dict_of_dicts(filename, delimiter):
    with open(filename, "r") as file:
        lines = file.read().splitlines()
        headers = lines[0].split(delimiter)
        return dict(zip(headers, [dict(zip(headers, x.split(delimiter))) for x in lines[1:]]))

def get_file_content_as_dict_of_dicts_with_first_column_as_key(filename, delimiter):
    with open(filename, "r") as file:
        lines = file.read().splitlines()
        headers = lines[0].split(delimiter)
        return {x.split(delimiter)[0]:dict(zip(headers, x.split(delimiter))) for x in lines[1:]}

def create_csv_file(filename, data, delimiter):
    with open(filename, "w") as file:
        file.write(delimiter.join(data[0].keys()) + "\n")
        for row in data:
            file.write(delimiter.join([str(x) for x in row.values()]) + "\n")

def create_csv_file_from_list_of_dicts(filename, data, delimiter):
    with open(filename, "w") as file:
        file.write(delimiter.join(data[0].keys()) + "\n")
        for row in data:
            file.write(delimiter.join([str(x) for x in row.values()]) + "\n")

def create_csv_file_from_dict_of_lists(filename, data, delimiter):
    with open(filename, "w") as file:
        file.write(delimiter.join(data.keys()) + "\n")
        for row in zip(*data.values()):
            file.write(delimiter.join([str(x) for x in row]) + "\n")

def create_csv_file_from_dict_of_dicts(filename, data, delimiter):
    with open(filename, "w") as file:
        file.write(delimiter.join(data.keys()) + "\n")
        for row in data.values():
            file.write(delimiter.join([str(x) for x in row.values()]) + "\n")

def create_csv_file_from_dict_of_dicts_with_first_column_as_key(filename, data, delimiter):
    with open(filename, "w") as file:
        file.write(delimiter.join(data[list(data.keys())[0]].keys()) + "\n")
        for row in data.values():
            file.write(delimiter.join([str(x) for x in row.values()]) + "\n")

def delete_file(filename):
    os.remove(filename)
