

def main(file_name):
    with open(file_name) as f:
        for line in f:
            print(line, end="")

if __name__ == '__main__':
    main("file.py")
