
import os
from sys import argv
import argparse

def parse_args():
	parser = argparse.ArgumentParser()
	parser.add_argument('-f', '--file', help='filename')
	parser.add_argument('-i', '--info', help='file information')
	parser.add_argument('-d', '--delete', help='delete file')
	args = parser.parse_args()
	return args

def file_info(args):
	for file in args.file:
		if os.path.exists(file):
			print(os.path.getsize(file))
		else:
			print('File not found')

def delete_file(args):
	for file in args.file:
		if os.path.exists(file):
			print(os.remove(file))
		else:
			print('File not found')


def main():
	args = parse_args()
	if args.file:
		if args.info:
			file_info(args)
		elif args.delete:
			delete_file(args)


if __name__ == '__main__':
	main()
