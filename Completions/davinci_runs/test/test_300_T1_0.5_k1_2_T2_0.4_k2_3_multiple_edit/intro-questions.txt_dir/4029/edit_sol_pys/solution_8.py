from sys import argv
#-----------------------------------------------------------------------------------------------------
def main():
    input_file = argv[1]
    output_file = argv[2]
    with open(input_file, 'r') as f:
        with open(output_file, 'w') as f2:
            f2.write(f.read())


if __name__ == '__main__':
    main()
