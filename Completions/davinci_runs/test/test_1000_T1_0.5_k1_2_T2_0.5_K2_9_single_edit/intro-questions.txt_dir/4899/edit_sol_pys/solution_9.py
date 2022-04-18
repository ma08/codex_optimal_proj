


def main():
    greeting = input("greeting: ").strip()
    new_greeting = greeting.replace('e', 'ee', 1) # replace the first 'e' with 'ee'
    print(new_greeting) # print the result


if __name__ == '__main__':
    main()
