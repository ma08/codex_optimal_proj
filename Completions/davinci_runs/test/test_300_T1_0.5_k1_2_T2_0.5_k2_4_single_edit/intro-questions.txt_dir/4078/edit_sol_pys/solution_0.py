def read_file(file_name):
    file = open(file_name, "r")
    file_content = file.read()
    file.close()
    return file_content

def write_file(file_name, content):
    file = open(file_name, "w")
    file.write(content)
    file.close()

def append_file(file_name, content):
    file = open(file_name, "a")
    file.write(content)
    file.close()

def read_file_line_by_line(file_name):
    file = open(file_name, "r")
    lines = file.readlines()
    file.close()
    return lines

def write_file_line_by_line(file_name, lines):
    file = open(file_name, "w")
    for line in lines:
        file.write(line)
    file.close()

def append_file_line_by_line(file_name, lines):
    file = open(file_name, "a")
    for line in lines:
        file.write(line)
    file.close()

def remove_new_line(lines):
    for i in range(len(lines)):
        lines[i] = lines[i][:-1]
    return lines

def remove_empty_line(lines):
    new_lines = []
    for line in lines:
        if line != "":
            new_lines.append(line)
    return new_lines

def split_line(line):
    return line.split()

def split_lines(lines):
    new_lines = []
    for line in lines:
        new_lines.append(line.split())
    return new_lines

def read_file_by_column(file_name):
    lines = read_file_line_by_line(file_name)
    lines = remove_new_line(lines)
    lines = remove_empty_line(lines)
    lines = split_lines(lines)
    return lines
