import os

class File(object):
    def __init__(self, filename):
        self.filename = filename
        self.file = None
        self.filedata = None
        self.filesize = 0
        self.filepos = 0
        self.filemode = None

    def open(self, mode):
        self.file = open(self.filename, mode)
        self.filemode = mode

    def read(self, size=None):
        if size is None:
            self.filedata = self.file.read()
            self.filesize = len(self.filedata)
        else:
            self.filedata = self.file.read(size)
            self.filesize = len(self.filedata)

    def write(self, data):
        self.file.write(data)

    def close(self):
        self.file.close()

    def seek(self, offset, whence=0):
        self.filepos = self.file.seek(offset, whence)

    def tell(self):
        return self.filepos

    def truncate(self, size=None):
        if size is None:
            self.file.truncate()
        else:
            self.file.truncate(size)

    def fstat(self):
        return self.file.fstat()

    def fsync(self):
        self.file.fsync()

    def flush(self):
        self.file.flush()

    def fileno(self):
        return self.file.fileno()

    def isatty(self):
        return self.file.isatty()

    def __iter__(self):
        return self.file.__iter__()

    def next(self):
        return self.file.next()

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.close()

    def __del__(self):
        self.close()

    def __str__(self):
        return '<File filename=%s, filemode=%s, filedata=%s>' % (self.filename, self.filemode, self.filedata)

    def __repr__(self):
        return self.__str__()
