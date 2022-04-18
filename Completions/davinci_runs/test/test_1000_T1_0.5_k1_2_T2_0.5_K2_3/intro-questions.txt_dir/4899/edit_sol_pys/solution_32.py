


def main():
    greeting = input('greeting: ').strip()  # strip() is used to remove whitespace
    new_greeting = greeting.replace('e', 'ee', 1) + '!'
    print('new greeting: ', new_greeting)


if __name__ == '__main__':
    main()
