import re

def fun(s):
    # return True if s is a valid email, else return False
    pattern = r'^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$' #r'^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$'
    return bool(re.match(pattern, s))

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input()) #3
    emails = []
    for _ in range(n):
        emails.append(input()) #lara@hackerrank.com
                               #brian-23@hackerrank.com
                               #britts_54@hackerrank.com

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
