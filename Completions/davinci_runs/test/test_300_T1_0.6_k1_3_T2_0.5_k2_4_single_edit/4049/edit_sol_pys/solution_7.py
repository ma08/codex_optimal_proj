from os import path
import csv


def read_csv(file_path):
    """
    Reads the CSV file at file_path to a list of dictionaries. Each
    dictionary maps the columns in the CSV to the values for that row.
    """
    output = []
    for row in csv.DictReader(open(file_path)):
        output.append(row)
    return output


def write_csv(file_path, rows):
    """
    Writes a CSV file at file_path using the list of dictionaries in rows.
    """
    with open(file_path, 'w') as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def read_file(file_path):
    """
    Reads the file at file_path to a string.
    """
    with open(file_path, 'r') as f:
        return f.read()


def write_file(file_path, contents):
    """
    Writes the given contents to the file at file_path.
    """
    with open(file_path, 'w') as f:
        f.write(contents)


def append_to_file(file_path, contents):
    """
    Appends the given contents to the file at file_path.
    """
    with open(file_path, 'a') as f:
        f.write(contents)


def file_exists(file_path):
    """
    Checks if a file exists at file_path.
    """
    return path.exists(file_path)


def folder_exists(folder_path):
    """
    Checks if a folder exists at folder_path.
    """
    return path.exists(folder_path)


def get_full_path(file_name, subfolder=None):
    """
    Returns the full path of a file in the given subfolder.
    If subfolder is None, returns the full path of file_name in the current
    working directory.
    """
    if subfolder:
        return path.join(subfolder, file_name)
    else:
        return path.join(path.curdir, file_name)
