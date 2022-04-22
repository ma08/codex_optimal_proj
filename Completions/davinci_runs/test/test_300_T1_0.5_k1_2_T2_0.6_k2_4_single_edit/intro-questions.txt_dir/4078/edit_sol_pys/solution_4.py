import argparse

parser = argparse.ArgumentParser(description="File utility")

parser.add_argument('-f', '--file', help="file name", required=True)
parser.add_argument('-m', '--mode', help="mode", required=True)

args = parser.parse_args()

try:
    f = open(args.file, args.mode)
    print("File opened sucessfully")
except IOError:
    print("File does not exist")
except Exception:
    print("Some other error")
finally:
    f.close()
