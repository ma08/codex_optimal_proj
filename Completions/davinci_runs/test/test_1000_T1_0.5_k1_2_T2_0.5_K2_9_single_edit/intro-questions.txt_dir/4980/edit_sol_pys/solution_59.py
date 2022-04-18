import re

def find_pink(n):
    count = 0
    for i in range(n):
        s = input()
        if re.search('pink', s.lower()) or re.search('rose', s.lower()):
            count += 1

    if count:
        return count
    else:
        return 'I must watch Star Wars with my daughter'

if __name__ == '__main__':
    n = int(input())
    print(find_pink(n))
