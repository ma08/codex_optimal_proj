"""

"""

import os


def list_directory(path=None):
    """

    :param path:
    :return:
    """
    if path is None:
        path = os.getcwd()

    return os.listdir(path)


def create_file(path, file_name):
    """

    :param path:
    :param file_name:
    :return:
    """
    if path is None:
        path = os.getcwd()

    if file_name is None:
        return

    file_path = os.path.join(path, file_name)
    if not os.path.exists(file_path):
        with open(file_path, 'w'):
            pass


def create_directory(path, directory_name):
    """

    :param path:
    :param directory_name:
    :return:
    """
    if path is None:
        path = os.getcwd()

    if directory_name is None:
        return

    directory_path = os.path.join(path, directory_name)
    if not os.path.exists(directory_path):
        os.mkdir(directory_path)


def delete_file(path, file_name):
    """

    :param path:
    :param file_name:
    :return:
    """
    if path is None:
        path = os.getcwd()

    if file_name is None:
        return

    file_path = os.path.join(path, file_name)
    if os.path.exists(file_path):
        os.remove(file_path)


def delete_directory(path, directory_name):
    """

    :param path:
    :param directory_name:
    :return:
    """
    if path is None:
        path = os.getcwd()

    if directory_name is None:
        return

    directory_path = os.path.join(path, directory_name)
    if os.path.exists(directory_path):
        os.rmdir(directory_path)


def check_directory_exists(path, directory_name):
    """

    :param path:
    :param directory_name:
    :return:
    """
    if path is None:
        path = os.getcwd()

    if directory_name is None:
        return False

    directory_path = os.path.join(path, directory_name)
    if os.path.exists(directory_path):
        return True

    return False


def check_file_exists(path, file_name):
    """

    :param path:
    :param file_name:
    :return:
    """
    if path is None:
        path = os.getcwd()

    if file_name is None:
        return False

    file_path = os.path.join(path, file_name)
    if os.path.exists(file_path):
        return True

    return False


def get_file_size(path, file_name):
    """

    :param path:
    :param file_name:
    :return:
    """
    if path is None:
        path = os.getcwd()

    if file_name is None:
        return False

    file_path = os.path.join(path, file_name)
    if os.path.exists(file_path):
        return os.path.getsize(file_path)

    return False


def get_file_content(path, file_name):
    """

    :param path:
    :param file_name:
    :return:
    """
    if path is None:
        path = os.getcwd()

    if file_name is None:
        return False

    file_path = os.path.join(path, file_name)
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            return f.read()

    return False
