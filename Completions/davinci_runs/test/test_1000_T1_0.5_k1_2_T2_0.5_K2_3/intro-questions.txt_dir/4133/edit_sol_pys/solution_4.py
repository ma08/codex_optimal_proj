

import re

def main():
    file = input()
    file = re.sub('[?()\.,:->]', '', file)
    file = re.sub('/', ' ', file)
    file = re.sub('\+', ' + ', file)
    file = re.sub('-', ' - ', file)
    file = re.sub('\*', ' * ', file)
    file = re.sub('[ \t]', '', file)
    file = re.sub('_', '0', file)
    if len(file) < 13 or len(file) > 1024:
        print('false')
        return
    for i in range(0, len(file)):
        if file[i] not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            print('false')
            return
    print(file)

if __name__ == '__main__':
    main()
