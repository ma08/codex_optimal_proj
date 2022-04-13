

def main():
    """
    This is the main function
    """
    num_inputs = int(input())
    num_list = []
    for _ in range(num_inputs):
        num_list.append(int(input()))
    print(sum(num_list))


if __name__ == "__main__":
    main()
