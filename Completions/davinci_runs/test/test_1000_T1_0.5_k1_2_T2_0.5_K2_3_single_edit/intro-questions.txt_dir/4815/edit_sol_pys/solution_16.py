import os
import sys


def list_files(path):
    """List all files in the given directory"""
    if not os.path.exists(path):
        raise Exception("Path not found")

    if os.path.isfile(path):
        raise Exception("Path is not a directory")

    return os.listdir(path)


def main():
    if len(sys.argv) < 2:
        print("Usage: python file.py <path>")
        sys.exit(1)

    path = sys.argv[1]
    try:
        files = list_files(path)
        for f in files:
            print(f)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
