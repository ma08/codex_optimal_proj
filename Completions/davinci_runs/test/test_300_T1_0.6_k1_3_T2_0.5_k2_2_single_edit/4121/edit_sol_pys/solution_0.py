import json
import os


class File:
    def __init__(self, path):
        self.path = path
        self.file_name = os.path.basename(path)
        self.content = {}
        self.read_file()

    def read_file(self):
        with open(self.path, 'r') as f:
            self.content = json.load(f)

    def get_value(self, key):
        return self.content.get(key, None)

    def get_value_by_path(self, path):
        key_list = path.split('.')
        value = self.get_value(key_list[0])
        if len(key_list) > 1:
            for key in key_list[1:]:
                value = value[key]
        return value

    def set_value(self, key, value):
        self.content[key] = value

    def set_value_by_path(self, path, value):
        key_list = path.split('.')
        self.set_value(key_list[0], value)
        if len(key_list) > 1:
            for key in key_list[1:]:
                self.set_value(key, value)

    def write_file(self):
        with open(self.path, 'w') as f:
            json.dump(self.content, f, indent=4)
