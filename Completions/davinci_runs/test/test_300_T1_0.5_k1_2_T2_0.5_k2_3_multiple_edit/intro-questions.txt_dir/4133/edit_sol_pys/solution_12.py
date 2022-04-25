

import re

def main():
    name = input()
    name = re.sub('[?()\.,:->]', '', name)
    name = re.sub('/', ' ', name)
    name = re.sub('\+', ' + ', name)
    name = re.sub('-', ' - ', name)
    name = re.sub('\*', ' * ', name)
    name = re.sub('_', '0', name)
    name = re.sub('\s+', ' ', name)
    name = name.strip()
    if len(name) < 13 or len(name) > 1024: return print('false')
    for i in range(0, len(name)):
        if name[i] not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            return print('false')
    print(name)

if __name__ == '__main__':
    main()
