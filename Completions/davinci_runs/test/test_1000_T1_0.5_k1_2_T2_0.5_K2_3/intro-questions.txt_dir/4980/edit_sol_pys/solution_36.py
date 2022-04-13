
import re

def find_pink(n, s):
    count = 0
    for i in range(n):
        if re.search('pink', s) or re.search('rose', s):
            count += 1

    if count:
        return count
    else:
        return 'I must watch Star Wars with my daughter'

if __name__ == '__main__':
    n = int(input())
    s = [input() for i in range(n)]
    s = s.lower()
    print(find_pink(n, s))
