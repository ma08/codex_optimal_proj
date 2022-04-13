
def main():
    greeting = input('Greeting: ').strip()
    new_greeting = greeting.replace('e', 'ee', 1)
    print('New greeting:', new_greeting)


if __name__ == '__main__':
    main()
