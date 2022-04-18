
from pprint import pprint

def main():
    with open('file.txt') as f:
        text = f.read()
    print(text)


if __name__ == "__main__":
    main()
