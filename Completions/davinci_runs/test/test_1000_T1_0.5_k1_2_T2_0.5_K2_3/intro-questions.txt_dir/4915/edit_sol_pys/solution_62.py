

def main():
    """
    The main function.
    """
    input_ = input()
    while input_ != '-1': # -1 is the exit condition
        input_ = input_.split()
        print(input_[0])
    print('-1')
        input_ = input()

if __name__ == '__main__':
    main()
