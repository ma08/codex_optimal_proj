import re

def find_pink(n):
    count = 0
    for _ in range(n):
        s = input()
        s = s.lower()  # convert to lowercase

        if re.search('pink', s) or re.search('rose', s):  # search for pinks and roses
            count += 1

    if count:
        return count
    else:
        return 'I must watch Star Wars with my daughter'  # if no pink, return this

if __name__ == '__main__':
    n = int(input())
    print(find_pink(n))
