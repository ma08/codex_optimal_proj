import os


def main():
    path = "."
    for root, dirs, files in os.walk(path):
        for f in files:
            print(f)


if __name__ == "__main__":
    main()
