
import re

if __name__ == '__main__':
    regex = r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"

    pattern = re.compile(regex, re.VERBOSE)
    for _ in range(int(input())):
        print(bool(pattern.match(input())))
