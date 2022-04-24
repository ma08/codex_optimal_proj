

def main(path):
    file = open(path, 'r')
    content = file.read()
    print(content)
    file.close()


if __name__ == '__main__':
    path = input('File path:')
    main(path)
