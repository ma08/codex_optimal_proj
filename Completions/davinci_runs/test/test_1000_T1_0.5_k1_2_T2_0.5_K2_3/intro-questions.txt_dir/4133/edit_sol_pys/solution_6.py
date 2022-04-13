

import re

def main():
    input_file = input()
    input_file = re.sub('[?()\.,:->]', '', input_file)
    input_file = re.sub('/', ' ', input_file)
    input_file = re.sub('\+', ' + ', input_file)
    input_file = re.sub('-', ' - ', input_file)
    input_file = re.sub('\*', ' * ', input_file)
    input_file = re.sub(' ', '', input_file)
    input_file = re.sub('_', '0', input_file)
    if len(input_file) < 13 or len(input_file) > 1024:
        print('false')
        return
    for i in range(0, len(input_file)):
        if input_file[i] not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            print('false')
            return
    print(input_file)

if __name__ == '__main__':
    main()
