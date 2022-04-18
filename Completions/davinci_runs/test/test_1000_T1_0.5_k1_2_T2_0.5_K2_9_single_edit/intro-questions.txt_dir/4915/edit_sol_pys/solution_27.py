

def main():
    """
    The main function.
    """
    input_ = input()
    while input_ != "-1":
        input_ = input_.split()
        print(input_[0])
        input_ = input()

if __name__ == '__main__':
    main()
