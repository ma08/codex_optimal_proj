import os
import shutil

source_path = r"C:\Users\jason\Documents\GitHub\python\source_path"
dest_path = r"C:\Users\jason\Documents\GitHub\python\dest_path"

def copy_file(source_path, dest_path):
	file_list = os.listdir(source_path)
	for file_name in file_list:
		shutil.copy(source_path + '/' + file_name, dest_path)

copy_file(source_path, dest_path)
