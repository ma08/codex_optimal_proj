import os


class File:
    """
    Class to handle files.
    """

    def __init__(self, path):
        """
        Constructor.
        :param path: The path to the file.
        """
        self.path = path
        self.file = None

    def open_file(self, mode):
        """
        Opens the file.
        :param mode: The mode to open the file in.
        """
        self.file = open(self.path, mode)

        self.file = open(self.path, mode)

    def close_file(self):
        """
        Closes the file.
        """
        self.file.close()

        self.file.close()

    def read_file(self):
        self.file = open(self.path, mode)
        """
        Reads the file.
        :return: The content of the file.
        """
        return self.file.read()

    def write_file(self, data):
        """
        Writes to the file.
        :param data: The data to write.
        """
        self.file.write(data)

        self.file.write(data)

    def exists(self):
        """
        Checks if the file exists.
        :return: True if the file exists, False otherwise.
        """
        return os.path.exists(self.path)
