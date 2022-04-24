

def plural(word):
    if word[-1] == 'y':
        return word[:-1] + 'ies'
    else:
        return word + 's'


def main():
    s = input()
    print(plural(s))


if __name__ == '__main__':
    main()
else:
    print(__name__)
