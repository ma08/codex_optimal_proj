

def main():
    """Main function"""
    input_string = input() # input string
    print("".join([input_string[i] for i in range(len(input_string)) if input_string[i].isupper()])) # printing the string

if __name__ == "__main__":
    main()
