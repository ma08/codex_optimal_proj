import os


class File:
    """
    Class to handle files.
    """

    def __init__(self, path):
        """
        Constructor.
        @param path: The path to the file.
        """
        self.path = path
        self.file = None

    def open(self, mode):
        """
        Opens the file.
        @param mode: The mode to open the file in.
        """
        self.file = open(self.path, mode)

    def close(self):
        """
        Closes the file.
        """
        self.file.close()

    def read(self):
        """
        Reads the file.
        @return: The content of the file.
        """
        return self.file.read()

    def write(self, data):
        """
        Writes to the file.
        @param data: The data to write.
        """
        self.file.write(data)

    def exists(self):
        """
        Checks if the file exists.
        @return: True if the file exists, False otherwise.
        """
        return os.path.exists(self.path)
