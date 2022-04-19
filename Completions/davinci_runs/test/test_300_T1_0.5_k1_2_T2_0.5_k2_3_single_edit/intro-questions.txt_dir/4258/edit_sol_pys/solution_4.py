from os import listdir
from os.path import isfile, join
import os
import re


class File(object):
    def __init__(self, file, file_name):
        self.file = file
        self.file_name = file_name

    def read_file(self):
        return open(self.file, "r")

    def write_file(self):
        return open(self.file, "w")

    def read_lines(self):
        return self.read_file().readlines()

    def read_file_string(self):
        return self.read_file().read()

    def write_file_string(self, string):
        self.write_file().write(string)

    def read_file_list(self):
        return self.read_file_string().split("\n")

    def write_file_list(self, list):
        self.write_file_string("\n".join(list))

    def add_text_to_file(self, text):
        self.write_file().write(text)

    def add_text_to_file_line(self, text, line_number):
        lines = self.read_file_list()
        lines[line_number] = text
        self.write_file_list(lines)

    def add_text_to_file_line_after(self, text, line_number):
        lines = self.read_file_list()
        lines.insert(line_number, text)
        self.write_file_list(lines)

    def add_text_to_file_line_before(self, text, line_number):
        lines = self.read_file_list()
        lines.insert(line_number-1, text)
        self.write_file_list(lines)

    def add_text_to_file_line_start(self, text, line_number):
        lines = self.read_file_list()
        lines[line_number] = text + lines[line_number]
        self.write_file_list(lines)

    def add_text_to_file_line_end(self, text, line_number):
        lines = self.read_file_list()
        lines[line_number] = lines[line_number] + text
        self.write_file_list(lines)

    def add_text_to_file_start(self, text):
        lines = self.read_file_list()
        lines[0] = text + lines[0]
        self.write_file_list(lines)

    def add_text_to_file_end(self, text):
        lines = self.read_file_list()
        lines[-1] = lines[-1] + text
        self.write_file_list(lines)

    def remove_line(self, line_number):
        lines = self.read_file_list()
        lines.pop(line_number)
        self.write_file_list(lines)

    def remove_line_start(self, line_number):
        lines = self.read_file_list()
        lines[line_number] = lines[line_number][1:]
        self.write_file_list(lines)

    def remove_line_end(self, line_number):
        lines = self.read_file_list()
        lines[line_number] = lines[line_number][:-1]
        self.write_file_list(lines)

    def remove_line_text(self, line_number, text):
        lines = self.read_file_list()
        lines[line_number] = lines[line_number].replace(text, "")
        self.write_file_list(lines)

    def remove_line_start_text(self, line_number, text):
        lines = self.read_file_list()
        lines[line_number] = lines[line_number].replace(text, "", 1)
        self.write_file_list(lines)

    def remove_line_end_text(self, line_number, text):
        lines = self.read_file_list()
        lines[line_number] = lines[line_number].rsplit(text, 1)[0]
        self.write_file_list(lines)

    def remove_file_text(self, text):
        lines = self.read_file_list()
        for line in lines:
            line.replace(text, "")
        self.write_file_list(lines)

    def remove_file_start_text(self, text):
        lines = self.read_file_list()
        for line in lines:
            line.replace(text, "", 1)
        self.write_file_list(lines)

    def remove_file_end_text(self, text):
        lines = self.read_file_list()
        for line in lines:
            line.rsplit(text, 1)[0]
        self.write_file_list(lines)

    def remove_file_start(self):
        lines = self.read_file_list()
        lines[0] = lines[0][1:]
        self.write_file_list(lines)

    def remove_file_end(self):
        lines = self.read_file_list()
        lines[-1] = lines[-1][:-1]
        self.write_file_list(lines)

    def add_file(self, file_to_add):
        with open(self.file, "a") as f:
            with open(file_to_add, "r") as f1:
                f.write(f1.read())

    def replace_file_text(self, text_to_replace, replacement_text):
        lines = self.read_file_list()
        for line in lines:
            line.replace(text_to_replace, replacement_text)
        self.write_file_list(lines)

    def replace_file_start_text(self, text_to_replace, replacement_text):
        lines = self.read_file_list()
        for line in lines:
            line.replace(text_to_replace, replacement_text, 1)
        self.write_file_list(lines)

    def replace_file_end_text(self, text_to_replace, replacement_text):
        lines = self.read_file_list()
        for line in lines:
            line.rsplit(text_to_replace, 1)[0] + replacement_text
        self.write_file_list(lines)

    def replace_line_text(self, line_number, text_to_replace, replacement_text):
        lines = self.read_file_list()
        lines[line_number].replace(text_to_replace, replacement_text)
        self.write_file_list(lines)

    def replace_line_start_text(self, line_number, text_to_replace, replacement_text):
        lines = self.read_file_list()
        lines[line_number].replace(text_to_replace, replacement_text, 1)
        self.write_file_list(lines)

    def replace_line_end_text(self, line_number, text_to_replace, replacement_text):
        lines = self.read_file_list()
        lines[line_number].rsplit(text_to_replace, 1)[0] + replacement_text
        self.write_file_list(lines)

    def replace_file(self, file_to_replace):
        lines = self.read_file_list()
        with open(file_to_replace, "r") as f:
