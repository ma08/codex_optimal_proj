

import re

def main():
    name = input('Enter the file name: ')
    name = re.sub('[?()\.,:-><]', '', name)
    name = re.sub('/', ' ', name)
    name = re.sub('\+', ' + ', name)
    name = re.sub('-', ' - ', name)
    name = re.sub('\*', ' * ', name)
    name = re.sub(' ', '', name)
    name = re.sub('_', '0', name)
    if len(name) < 13 or len(name) > 1024 or name[0] == '0':
        print('False')
        return
    for i in range(0, len(name)):
        if name[i] not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-']:
            print('False')
            return
    print('True')

if __name__ == '__main__':
    main()
