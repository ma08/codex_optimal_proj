import os

def write_file(filename, data):
	with open(filename, "w") as f:
		f.write(data)

def read_file(filename):
	with open(filename, "r") as f:
		return f.read()

def create_file(filename):
	try:
		with open(filename, "x") as f:
			f.write("")
			print("File created successfully")
	except FileExistsError:
		print("File already exists")

def delete_file(filename):
	if os.path.exists(filename):
		os.remove(filename)
		print("File deleted successfully")
	else:
		print("File not found")









