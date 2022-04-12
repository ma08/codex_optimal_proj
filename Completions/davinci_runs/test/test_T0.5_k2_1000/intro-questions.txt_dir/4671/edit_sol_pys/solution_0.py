

import re

def fun(s):
    # return True if s is a valid email, else return False
    if re.match(r'[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$', s) is not None:
        return True
    else:
        return False

if __name__ == '__main__':
    n = int(input())
    emails = [input() for _ in range(n)]
    filtered_emails = list(filter(fun, emails))
    filtered_emails.sort()
    print(filtered_emails)
