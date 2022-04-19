

import re

def main():
    name = input()
    name = re.sub('[?()\.,:->+-]', '', name)
    name = re.sub('/', ' ', name)
    name = re.sub('\*', ' * ', name)
    name = re.sub('_', '0', name)
    print(name.replace(' ', ''))

if __name__ == '__main__':
    main()
