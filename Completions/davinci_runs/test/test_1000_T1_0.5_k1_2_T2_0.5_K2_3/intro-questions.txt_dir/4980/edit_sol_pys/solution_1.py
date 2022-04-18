
import re

def find_pink(n, s):
    count = 0
    for i in range(n):
        if re.search('pink', s[i]) or re.search('rose', s[i]):
            count += 1

    if count:
        return count
    else:
        return 'I must watch Star Wars with my daughter'

if __name__ == '__main__':
    n = int(input())
    s = input()
    s = s.lower()
    print(find_pink(n, s))
