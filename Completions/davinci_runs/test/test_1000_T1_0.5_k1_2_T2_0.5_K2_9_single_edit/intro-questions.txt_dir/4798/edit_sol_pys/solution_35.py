
def main():
    """Main function"""
    input_string = input()
    print("".join([input_string[i] for i in range(len(input_string)) if input_string[i].isupper()]))


if __name__ == "__main__":
    main()
