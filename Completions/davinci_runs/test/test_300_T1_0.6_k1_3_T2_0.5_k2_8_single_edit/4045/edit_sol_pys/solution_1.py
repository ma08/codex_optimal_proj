import os
import sys
import re
import math

def read_file(filename):
	f = open(filename, 'r')
	content = f.read()
	f.close()
	return content

def write_file(filename, content):
	f = open(filename, 'w')
	f.write(content)
	f.close()

def get_file_size(filename):
	return os.path.getsize(filename)

def get_file_name(filename):
	return os.path.basename(filename)

def get_file_path(filename):
	return os.path.dirname(filename)

def get_file_extension(filename):
	return os.path.splitext(filename)[1][1:]

def get_file_name_without_extension(filename):
	return os.path.splitext(filename)[0]

def get_file_list(path):
	return os.listdir(path)

def get_file_list_with_extension(path, extension):
	file_list = []
	for file in get_file_list(path):
		if get_file_extension(file) == extension:
			file_list.append(file)
	return file_list

def get_file_list_without_extension(path, extension):
	file_list = []
	for file in get_file_list(path):
		if get_file_extension(file) != extension:
			file_list.append(file)
	return file_list

def get_file_list_with_regex(path, regex):
	file_list = []
	for file in get_file_list(path):
		if re.search(regex, file):
			file_list.append(file)
	return file_list

def get_file_list_without_regex(path, regex):
	file_list = []
	for file in get_file_list(path):
		if not re.search(regex, file):
			file_list.append(file)
	return file_list

def get_file_list_with_size_greater_than(path, size):
	file_list = []
	for file in get_file_list(path):
		if get_file_size(file) > size:
			file_list.append(file)
	return file_list

def get_file_list_with_size_less_than(path, size):
	file_list = []
	for file in get_file_list(path):
		if get_file_size(file) < size:
			file_list.append(file)
	return file_list

def get_file_list_with_size_between(path, min_size, max_size):
	file_list = []
	for file in get_file_list(path):
		if get_file_size(file) > min_size and get_file_size(file) < max_size:
			file_list.append(file)
	return file_list

def get_file_list_with_size_closest_to(path, size):
	file_list = []
	for file in get_file_list(path):
		if math.fabs(get_file_size(file) - size) < math.fabs(get_file_size(file_list[0]) - size):
			file_list.append(file)
	return file_list

def get_file_list_with_size_farthest_to(path, size):
	file_list = []
	for file in get_file_list(path):
		if math.fabs(get_file_size(file) - size) > math.fabs(get_file_size(file_list[0]) - size):
			file_list.append(file)
	return file_list

def get_file_list_with_size_closest_to_multiple(path, size):
	file_list = []
	for file in get_file_list(path):
		if get_file_size(file) % size == 0:
			file_list.append(file)
	return file_list

def get_file_list_with_size_farthest_to_multiple(path, size):
	file_list = []
	for file in get_file_list(path):
		if get_file_size(file) % size != 0:
			file_list.append(file)
	return file_list
