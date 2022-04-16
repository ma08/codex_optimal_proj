

def main():
    """
    The main function.
    """
    input_ = input()
    while input_ != '-1': # pylint: disable=W0612
        input_ = input_.split()
        print(input_) # pylint: disable=C0325
        input_ = input()

if __name__ == '__main__':
    main()
