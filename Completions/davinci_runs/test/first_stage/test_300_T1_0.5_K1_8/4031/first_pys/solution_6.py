

# Solution 1
# def is_substring(string1, string2):
#     if len(string1) > len(string2):
#         return False
#     for i in range(len(string2) - len(string1) + 1):
#         if string1 == string2[i:i+len(string1)]:
#             return True
#     return False
#
#
# def is_substring_2(string1, string2):
#     if len(string1) > len(string2):
#         return False
#     return string1 in string2
#
#
# if __name__ == "__main__":
#     n = int(input())
#     strings = []
#     for _ in range(n):
#         strings.append(input())
#
#     for i in range(n):
#         for j in range(i+1, n):
#             if is_substring(strings[i], strings[j]):
#                 strings[i], strings[j] = strings[j], strings[i]
#
#     for i in range(n):
#         for j in range(i+1, n):
#             if not is_substring(strings[i], strings[j]):
#                 print("NO")
#                 exit()
#     print("YES")
#     for s in strings:
#         print(s)

# Solution 2
# def is_substring(string1, string2):
#     if len(string1) > len(string2):
#         return False
#     for i in range(len(string2) - len(string1) + 1):
#         if string1 == string2[i:i+len(string1)]:
#             return True
#     return False
#
#
# if __name__ == "__main__":
#     n = int(input())
#     strings = []
#     for _ in range(n):
#         strings.append(input())
#
#     for i in range(n):
#         for j in range(i+1, n):
#             if is_substring(strings[i], strings[j]):
#                 strings[i], strings[j] = strings[j], strings[i]
#
#     for i in range(n):
#         for j in range(i+1, n):
#             if not is_substring(strings[i], strings[j]):
#                 print("NO")
#                 exit()
#     print("YES")
#     for s in strings:
#         print(s)

# Solution 3
def is_substring(string1, string2):
    if len(string1) > len(string2):
        return False
    for i in range(len(string2) - len(string1) + 1):
        if string1 == string2[i:i+len(string1)]:
            return True
    return False


def is_substring_2(string1, string2):
    if len(string1) > len(string2):
        return False
    return string1 in string2


def is_substring_3(string1, string2):
    if len(string1) > len(string2):
        return False
    return string2.startswith(string1)


def is_substring_4(string1, string2):
    if len(string1) > len(string2):
        return False
    return string2.endswith(string1)


if __name__ == "__main__":
    n = int(input())
    strings = []
    for _ in range(n):
        strings.append(input())

    for i in range(n):
        for j in range(i+1, n):
            if is_substring_4(strings[i], strings[j]):
                strings[i], strings[j] = strings[j], strings[i]

    for i in range(n):
        for j in range(i+1, n):
            if not is_substring_3(strings[i], strings[j]):
                print("NO")
                exit()
    print("YES")
    for s in strings:
        print(s)