import os


def read_file_into_string(input_file, from_ord, to_ord):
    """
    Open and read a file, return the data in a string.
    Takes input_file and returns a lowercase string.
    """
    input_file = os.path.abspath(os.path.expanduser(input_file))
    with open(input_file, "r") as f:
        data = f.read().lower()
    return (data[from_ord:to_ord])


def get_string_list_from_file(input_file, from_ord, to_ord):
    """
    Open and read a file, return a list of strings.
    Takes input_file and returns a list of lowercase strings.
    """
    data = read_file_into_string(input_file, from_ord, to_ord).split("\n")
    return data


def get_string_list_from_filename(input_file, from_ord, to_ord):
    """
    Open and read a file, return a list of strings.
    Takes input_file and returns a list of lowercase strings.
    """
    data = read_file_into_string(input_file, from_ord, to_ord).split("\n")
    return data


def get_filename_list_from_dir(input_dir):
    """
    Reads a directory of files and returns a list of filenames
    """
    input_dir = os.path.abspath(os.path.expanduser(input_dir))
    data = os.listdir(input_dir)
    return data
