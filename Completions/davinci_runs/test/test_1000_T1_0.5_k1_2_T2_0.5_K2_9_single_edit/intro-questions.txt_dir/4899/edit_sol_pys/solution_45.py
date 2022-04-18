


def main():
    greeting = input().strip()  # strip removes leading and trailing whitespace
    new_greeting = greeting.replace('e', 'ee', 1)
    print(new_greeting)


if __name__ == '__main__':
    main()
