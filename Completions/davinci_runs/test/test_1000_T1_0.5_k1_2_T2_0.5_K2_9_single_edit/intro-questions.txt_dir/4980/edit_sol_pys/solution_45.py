
import re

def find_pink(n):
    count = 0
    for i in range(n):
        s = input()
        s = s.lower()

        if re.search('pink', s) or re.search('rose', s):
            count += 1

    if count:
        return count
    else:
        return -1

if __name__ == '__main__':
    n = int(input())
    print('I must watch Star Wars with my daughter' if find_pink(n) == -1 else find_pink(n))
