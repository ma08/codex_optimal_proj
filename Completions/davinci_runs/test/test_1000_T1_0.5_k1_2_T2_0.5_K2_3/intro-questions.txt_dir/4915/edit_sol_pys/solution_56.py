

def main():
    """
    The main function.
    """
    input_file_name = input()
    while input_file_name != '-1':
        input_file_name = input_file_name.split(',')
        print(input_file_name)
        input_file_name = input()

if __name__ == '__main__':
    main()
