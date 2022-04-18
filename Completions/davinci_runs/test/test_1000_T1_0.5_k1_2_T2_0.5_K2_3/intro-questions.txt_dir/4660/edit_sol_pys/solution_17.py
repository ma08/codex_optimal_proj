
import re

def fun(s):
    # return True if s is a valid email, else return False
    a = re.match(r'[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$', s)
    return(a)

def filter_mail(emails):
    return list(filter(fun, emails)) # filter takes a function and an iterable as arguments and returns an iterator

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails) # returns list of valid emails
filtered_emails.sort() # sort the list
print(filtered_emails) # print the list
