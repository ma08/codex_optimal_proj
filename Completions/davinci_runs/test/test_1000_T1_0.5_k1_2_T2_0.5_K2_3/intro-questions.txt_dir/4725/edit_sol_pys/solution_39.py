

def main():
    word = input()  # get input from user
    if len(set(word)) <= 2:  # if the length of the set of the input is less than or equal to 2
        print(0)
    else:
        print(len(word) - 2)  # else print the length of the input minus 2

if __name__ == "__main__":
    main()
