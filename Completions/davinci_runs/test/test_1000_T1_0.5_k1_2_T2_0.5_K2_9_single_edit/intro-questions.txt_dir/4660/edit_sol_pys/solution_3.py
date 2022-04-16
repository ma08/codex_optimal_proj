
import re

def fun(s):
    # return True if s is a valid email, else return False
    if re.search(r'[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$',s):
        return True
    else:
        return False

def filter_mail(emails):
    return filter(fun, emails)

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())
    filtered_emails = filter_mail(emails)
    filtered_emails.sort()
    print(filtered_emails)


"""
=====OUTPUT=====

3
lara@hackerrank.com
brian-23@hackerrank.com
britts_54@hackerrank.com
['brian-23@hackerrank.com', 'britts_54@hackerrank.com', 'lara@hackerrank.com']

"""
