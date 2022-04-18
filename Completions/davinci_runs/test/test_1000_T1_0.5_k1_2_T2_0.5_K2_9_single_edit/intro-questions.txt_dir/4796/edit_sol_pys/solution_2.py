

def main():
    # Get the input and put it in a list
    input_list = list(map(int, input().split()))
    # Convert the list to a set
    unique_list = set(input_list)
    # Find the number of unique elements in the set
    print(len(unique_list))

if __name__ == '__main__':
    main()
