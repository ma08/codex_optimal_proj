


def pluralize(s):
    if s[-1] == 's':
        return s + 'es'
    else:
        return s + 's'


if __name__ == '__main__':
    s = input()
    print(pluralize(s))
