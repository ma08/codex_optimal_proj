#!/usr/bin/env python

import os
import sys
import csv
import gzip
import bz2
import zipfile


class File(object):
    """
    File class
    """
    def __init__(self, filename):
        self.filename = filename
        self.ext = os.path.splitext(filename)[1].lower()
        self.file = None

    def open(self, mode='r', encoding='utf-8'):
        if self.ext == '.gz':
            self.file = gzip.open(self.filename, mode=mode, encoding=encoding)
        elif self.ext == '.bz2':
            self.file = bz2.open(self.filename, mode=mode, encoding=encoding)
        elif self.ext == '.zip':
            self.file = zipfile.ZipFile(self.filename, mode=mode, compression=zipfile.ZIP_DEFLATED)
        else:
            self.file = open(self.filename, mode=mode, encoding=encoding)

    def close(self):
        if self.file:
            self.file.close()

    def __enter__(self):
        self.open()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def __iter__(self):
        return self

    def __next__(self):
        return self.file.__next__()

    def __getattr__(self, attr):
        return getattr(self.file, attr)


class CSV(File):
    def __init__(self, filename, dialect='excel', **kwargs):
        super().__init__(filename)
        self.dialect = dialect
        self.kwargs = kwargs

    def open(self, mode='r', encoding='utf-8'):
        super().open(mode=mode, encoding=encoding)
        if self.file:
            self.reader = csv.reader(self.file, dialect=self.dialect, **self.kwargs)
            self.writer = csv.writer(self.file, dialect=self.dialect, **self.kwargs)

    def __iter__(self):
        return self.reader

    def __next__(self):
        return self.reader.__next__()

    def write_row(self, row):
        self.writer.writerow(row)

    def write_rows(self, rows):
        self.writer.writerows(rows)


def main():
    filename = sys.argv[1]
    with CSV(filename) as csv_file:
        for row in csv_file:
            print(row)


if __name__ == '__main__':
    main()
