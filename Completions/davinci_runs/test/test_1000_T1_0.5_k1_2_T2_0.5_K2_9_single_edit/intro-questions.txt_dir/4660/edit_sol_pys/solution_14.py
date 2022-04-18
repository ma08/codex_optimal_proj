
import os
import sys
import re

def fun(s):
    # return True if s is a valid email, else return False
    pattern = r'^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.\w{1,3}$'
    return re.match(pattern, s)

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    emails = []
    for _ in range(n):
        emails.append(sys.stdin.readline())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)


"""
=====OUTPUT=====


['brian-23@hackerrank.com', 'britts_54@hackerrank.com', 'lara@hackerrank.com']

"""
