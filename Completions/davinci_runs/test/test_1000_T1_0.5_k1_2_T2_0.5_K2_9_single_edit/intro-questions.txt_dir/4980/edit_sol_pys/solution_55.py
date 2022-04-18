import re


def find_pink(n):
    '''
    find the number of pink items
    '''
    count = 0
    for i in range(n):
        s = input()
        s = s.lower()

        if re.search('pink', s) or re.search('rose', s):
            count += 1

    if count:

        return count
    else:
        return 'I must watch Star Wars with my daughter'

if __name__ == '__main__':
    n = int(input())
    print(find_pink(n))
