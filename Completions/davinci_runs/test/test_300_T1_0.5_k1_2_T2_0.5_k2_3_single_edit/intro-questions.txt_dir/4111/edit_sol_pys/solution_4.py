import re

def check_email(email):
    if re.match(r'^[a-zA-Z0-9+\-_]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]+$', email):
        return True
    else:
        return False

def check_name(name):
    if re.match(r'^[a-zA-Z0-9]+$', name):
        return True
    else:
        return False

def check_password(password):
    if re.match(r'^[a-zA-Z0-9+\-_]+$', password):
        return True
    else:
        return False

def check_username(username):
    if re.match(r'^[a-zA-Z0-9+\-_]+$', username):
        return True
    else:
        return False

def check_phone(phone):
    if re.match(r'^[0-9]{3}-[0-9]{4}-[0-9]{4}$', phone):
        return True
    else:
        return False

def check_date(date):
    if re.match(r'^[0-9]{4}-[0-9]{2}-[0-9]{2}$', date):
        return True
    else:
        return False

email = input()
name = input()
password = input()
username = input()
phone = input()
date = input()

print(check_email(email))
print(check_name(name))
print(check_password(password))
print(check_username(username))
print(check_phone(phone))
print(check_date(date))


# n = int(input())
# a = list(map(int,input().split()))

# # def find_good_candies(n, a):
# #     sum_odd, sum_even = 0, 0
# #     for i in range(1,n):
# #         if i%2 == 0:
# #             sum_even += a[i]
# #         else:
# #             sum_odd += a[i]
# #     if sum_odd == sum_even:
# #         return 1
# #     else:
# #         return 0

# # ans = 0
# # for i in range(n):
# #     ans += find_good_candies(n, a[:i] + a[i+1:])

# # print(ans)

# odd, even = 0, 0
# for i in range(n):
#     if i%2 == 0:
#         odd += a[i]
#     else:
#         even += a[i]

# ans = 0
# for i in range(n):
#     if i%2 == 0:
#         if odd - a[i] == even:
#             ans += 1
#     else:
#         if odd == even - a[i]:
#             ans += 1

# print(ans)
