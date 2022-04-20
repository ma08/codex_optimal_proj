
import os
import sys
import shutil
import argparse
import configparser


def get_parser():
    parser = argparse.ArgumentParser(description="A simple file organizer")
    parser.add_argument("path", help="Path to the file or directory")

    return parser


def get_file_extension(path):
    return os.path.splitext(path)[1][1:]


def get_config():
    config = configparser.ConfigParser()
    config.read("config.ini")

    return config


def move_file(path, extension):
    config = get_config()
    destination = config["DEFAULT"][extension]

    if not destination:
        return False

    destination = os.path.join(os.path.dirname(path), destination)

    if not os.path.exists(destination):
        os.makedirs(destination)

    shutil.move(path, destination)

    return True


def organize(path):
    if os.path.isfile(path):
        extension = get_file_extension(path)
        move_file(path, extension)

    elif os.path.isdir(path):
        for file in os.listdir(path):
            organize(os.path.join(path, file))

    else:
        print("Invalid path")
        sys.exit(1)


def main():
    parser = get_parser()
    args = parser.parse_args()

    organize(args.path)


if __name__ == '__main__':
    main()
