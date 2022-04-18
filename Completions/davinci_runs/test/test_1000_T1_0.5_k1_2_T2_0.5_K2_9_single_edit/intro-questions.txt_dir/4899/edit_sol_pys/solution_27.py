


def main():
    greeting = input().strip() # strip() removes spaces
    new_greeting = greeting.replace('e', 'ee', 1) #replace the first 'e' with 'ee'
    print(new_greeting) #print the new greeting


if __name__ == '__main__':
    main()
