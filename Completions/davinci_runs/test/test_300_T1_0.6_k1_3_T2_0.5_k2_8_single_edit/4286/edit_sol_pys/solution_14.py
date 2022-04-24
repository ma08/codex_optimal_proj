
import os


def main():
    os.system("mkdir -p /tmp/test")
    os.system("touch /tmp/test/file.txt")
    os.system("echo 'Hello' > /tmp/test/file.txt")


if __name__ == "__main__":
    main()
