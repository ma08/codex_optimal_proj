

import re

def main():
    name = input()
    name = re.sub('[?()\.,:->]', '', name) # remove special characters
    name = re.sub('/', ' ', name) # replace / with space
    name = re.sub('\+', ' + ', name) # replace + with +
    name = re.sub('-', ' - ', name) # replace - with -
    name = re.sub('\*', ' * ', name) # replace * with *
    name = re.sub(' ', '', name) # remove spaces
    name = re.sub('_', '0', name) # replace _ with 0
    if len(name) < 13 or len(name) > 1024:
        print('false')
        return
    for i in range(0, len(name)):
        if name[i] not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            print('false')
            return
    print(name)

if __name__ == '__main__':
    main()
