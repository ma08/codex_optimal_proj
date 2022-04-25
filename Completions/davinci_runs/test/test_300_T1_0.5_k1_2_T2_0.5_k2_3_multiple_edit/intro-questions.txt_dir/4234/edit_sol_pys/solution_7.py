import re


def solution(s):
    s = re.sub(r'[^a-zA-Z]', '', s)
    s = s.lower()
    s = s.replace(' ', '')
    return s == s[::-1]


print(solution('A man, a plan, a canal: Panama'))
