

def main():
    """
    The main function.
    """
    input_ = input()
    while input_ != '-1': #when -1 is entered, the program terminates
        input_ = input_.split()
        print(input_) #prints the input
        input_ = input()

if __name__ == '__main__':
    main()
