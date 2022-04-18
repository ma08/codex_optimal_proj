import sys



def main():
    if len(sys.argv) < 2:
        print('Please give a file name')
        sys.exit(1)

    file_name = sys.argv[1]

    try:
        file_object = open(file_name)
    except IOError:
        print("Sorry, can't open file: " + file_name)
        sys.exit(1)

    for line in file_object:
        print(line, end='')

    file_object.close()

if __name__ == "__main__":
    main()
