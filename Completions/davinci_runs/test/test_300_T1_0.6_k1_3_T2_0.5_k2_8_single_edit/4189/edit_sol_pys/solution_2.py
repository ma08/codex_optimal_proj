import os
import shutil


class File(object):
    def __init__(self, file_path):
        self.file_path = file_path

    def read(self):
        with open(self.file_path, 'r') as f:
            return f.read()

    def write(self, content):
        with open(self.file_path, 'w') as f:
            return f.write(content)

    def write_lines(self, lines):
        with open(self.file_path, 'w') as f:
            return f.writelines(lines)

    def append(self, content):
        with open(self.file_path, 'a') as f:
            return f.write(content)

    def append_lines(self, lines):
        with open(self.file_path, 'a') as f:
            return f.writelines(lines)

    def read_lines(self):
        with open(self.file_path, 'r') as f:
            return f.readlines()

    def copy(self, new_path):
        shutil.copy(self.file_path, new_path)

    def move(self, new_path):
        shutil.move(self.file_path, new_path)

    def remove(self):
        os.remove(self.file_path)

    @property
    def size(self):
        return os.path.getsize(self.file_path)

    @property
    def exists(self):
        return os.path.exists(self.file_path)

    @property
    def is_file(self):
        return os.path.isfile(self.file_path)

    @property
    def is_directory(self):
        return os.path.isdir(self.file_path)

    @property
    def is_link(self):
        return os.path.islink(self.file_path)

    @property
    def is_mount(self):
        return os.path.ismount(self.file_path)

    @property
    def atime(self):
        return os.path.getatime(self.file_path)

    @property
    def mtime(self):
        return os.path.getmtime(self.file_path)

    @property
    def ctime(self):
        return os.path.getctime(self.file_path)

    @property
    def extension(self):
        return os.path.splitext(self.file_path)[1]

    @property
    def name(self):
        return os.path.basename(self.file_path)

    @property
    def directory(self):
        return os.path.dirname(self.file_path)

    @property
    def parent_directory(self):
        return os.path.dirname(os.path.dirname(self.file_path))


class Directory(object):
    def __init__(self, directory_path):
        self.directory_path = directory_path

    def create(self):
        os.makedirs(self.directory_path)

    def remove(self):
        shutil.rmtree(self.directory_path)

    def move(self, new_path):
        shutil.move(self.directory_path, new_path)

    def copy(self, new_path):
        shutil.copytree(self.directory_path, new_path)

    @property
    def files(self):
        return [File(os.path.join(self.directory_path, f)) for f in os.listdir(self.directory_path) if
                os.path.isfile(os.path.join(self.directory_path, f))]

    @property
    def directories(self):
        return [Directory(os.path.join(self.directory_path, d)) for d in os.listdir(self.directory_path) if
                os.path.isdir(os.path.join(self.directory_path, d))]

    @property
    def exists(self):
        return os.path.exists(self.directory_path)

    @property
    def is_directory(self):
        return os.path.isdir(self.directory_path)

    @property
    def is_link(self):
        return os.path.islink(self.directory_path)

    @property
    def is_mount(self):
        return os.path.ismount(self.directory_path)

    @property
    def atime(self):
        return os.path.getatime(self.directory_path)

    @property
    def mtime(self):
        return os.path.getmtime(self.directory_path)

    @property
    def ctime(self):
        return os.path.getctime(self.directory_path)

    @property
    def name(self):
        return os.path.basename(self.directory_path)

    @property
    def directory(self):
        return os.path.dirname(self.directory_path)

    @property
    def parent_directory(self):
        return os.path.dirname(os.path.dirname(self.directory_path))
