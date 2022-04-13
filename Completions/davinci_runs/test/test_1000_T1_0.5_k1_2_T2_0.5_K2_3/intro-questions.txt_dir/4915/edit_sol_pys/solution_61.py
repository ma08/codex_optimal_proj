
def main():
    """
    The main function.
    """
    input_ = input().split()
    while input_[0] != '-1':
        print(input_[0])
        input_ = input().split()

if __name__ == '__main__':
    main()
