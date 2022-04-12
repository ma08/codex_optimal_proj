

def main():
    """
    The main function.
    """
    input_line = input()
    while input_line != '-1': 
        input_line = input_line.split()
        print(input_line)
        input_line = input()

if __name__ == '__main__':
    main()
