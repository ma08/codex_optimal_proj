

import re

def main():
    file_name = input()
    file_name = re.sub('[?()\.,:->]', '', file_name)
    file_name = re.sub('/', ' ', file_name)
    file_name = re.sub('\+', ' + ', file_name)
    file_name = re.sub('-', ' - ', file_name)
    file_name = re.sub('\*', ' * ', file_name)
    file_name = re.sub(' ', '', file_name)
    file_name = re.sub('_', '0', file_name)
    if len(file_name) < 13 or len(file_name) > 1024:
        print('false')
        return
    for i in range(0, len(file_name)):
        if file_name[i] not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            print('false')
            return
    print(file_name)

if __name__ == '__main__':
    main()
