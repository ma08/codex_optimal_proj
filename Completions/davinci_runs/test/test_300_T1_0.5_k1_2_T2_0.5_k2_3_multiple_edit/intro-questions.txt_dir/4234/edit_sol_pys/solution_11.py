



def read_file(file_name):
    with open(file_name) as f:
        return f.read()


def write_file(file_name, data):
    with open(file_name, 'w') as f:
        f.write(data)


def append_file(file_name, data):
    with open(file_name, 'a') as f:
        f.write(data)


def read_file_by_line(file_name):
    with open(file_name) as f:
        for line in f:
            yield line


def read_file_by_line_with_strip(file_name):
    with open(file_name) as f:
        for line in f:
            yield line.strip()


def read_file_by_line_with_split(file_name, sep=None):
    with open(file_name) as f:
        for line in f:
            yield line.split(sep=sep)


def read_file_by_line_with_strip_and_split(file_name, sep=None):
    with open(file_name) as f:
        for line in f:
            yield line.strip().split(sep=sep)

import sys

n = int(sys.stdin.readline())
s = sys.stdin.readline().strip()

stack = []
for i in range(n):
    stack.append(s[i])
    if len(stack) >= 2 and stack[-1] == stack[-2]:
        stack.pop()
        stack.pop()

print(n - len(stack))
print(''.join(stack))
