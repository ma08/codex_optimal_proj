import os
import fnmatch


def find(pattern, path):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
    return result


def find2(pattern, path):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if pattern in name:
                result.append(os.path.join(root, name))
    return result


def find3(pattern, path):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if pattern in name:
                result.append(os.path.join(root, name))
    return result
