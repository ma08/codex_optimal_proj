import re
import requests


url = "https://www.yahoo.com"
response = requests.get(url)
data = response.text
#print(data)

#findall = re.findall(r"\w+", data)
#print(findall)


#s = input()
#
#if s[1] == s[2] or s[2] == s[3] or s[3] == s[4]:
#    print("Bad")
#else:
#    print("Good")
#
#
#
#s = input()
#
#if s[1] == s[2] or s[2] == s[3] or s[3] == s[4]:
#    print("Bad")
#else:
#    print("Good")
