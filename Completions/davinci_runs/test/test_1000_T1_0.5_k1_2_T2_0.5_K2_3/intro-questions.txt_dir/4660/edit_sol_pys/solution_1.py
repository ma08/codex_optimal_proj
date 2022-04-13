import re

def fun(s):
    # return True if s is a valid email, else return False
    a = re.match(r'[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$', s) #regular expression
    return(a) #returning the value

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input("Enter the number of emails you want to enter: "))
    emails = []
    for _ in range(n):
        emails.append(input("Enter the email: "))

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print("The valid email addresses are :",filtered_emails)
