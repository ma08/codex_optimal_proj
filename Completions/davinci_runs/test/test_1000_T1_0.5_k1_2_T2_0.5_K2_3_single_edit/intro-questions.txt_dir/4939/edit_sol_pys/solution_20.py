

# Program starts here
# n, k = map(int, input().split())
# commands = input().split()

# egg = 0

# for i in range(len(commands)):
#     if "undo" in commands[i]:
#         for j in range(int(commands[i][5:])):
#             if i - j - 1 >= 0:
#                 egg -= int(commands[i-j-1])
#             elif i - j - 1 < 0:
#                 egg -= int(commands[0])
#     else:
#         egg += int(commands[i])

# print(egg % n)



def check(s, k):
    # print(s)
    # print(k)
    if s == k:
        return True
    return False


def check_valid(s):
    if s[0] == s[1] and s[1] == s[2] and s[2] == s[3]:
        return False
    return True


def check_valid_2(s):
    if s[0] == s[1] and s[1] == s[2]:
        return False
    return True


def check_valid_3(s):
    if s[1] == s[2] and s[2] == s[3]:
        return False
    return True


def check_valid_4(s):
    if s[0] == s[1] and s[2] == s[3]:
        return False
    return True


def check_valid_5(s):
    if s[0] == s[2] and s[1] == s[3]:
        return False
    return True


def check_valid_6(s):
    if s[0] == s[3] and s[1] == s[2]:
        return False
    return True


def check_valid_7(s):
    if s[0] == s[1] or s[1] == s[2] or s[2] == s[3]:
        return False
    return True


def check_valid_8(s):
    if s[0] == s[2] or s[1] == s[3]:
        return False
    return True


def check_valid_9(s):
    if s[0] == s[3]:
        return False
    return True


def check_valid_10(s):
    if s[0] == s[1] or s[1] == s[2] or s[2] == s[3]:
        return False
    return True


def check_valid_11(s):
    if s[0] == s[2] or s[1] == s[3]:
        return False
    return True


def check_valid_12(s):
    if s[0] == s[3]:
        return False
    return True


def check_valid_13(s):
    if s[0] == s[1] or s[1] == s[2] or s[2] == s[3]:
        return False
    return True


def check_valid_14(s):
    if s[0] == s[2] or s[1] == s[3]:
        return False
    return True


def check_valid_15(s):
    if s[0] == s[3]:
        return False
    return True


def check_valid_16(s):
    if s[0] == s[1] or s[1] == s[2] or s[2] == s[3]:
        return False
    return True


def check_valid_17(s):
    if s[0] == s[2] or s[1] == s[3]:
        return False
    return True


def check_valid_18(s):
    if s[0] == s[3]:
        return False
    return True


def check_valid_19(s):
    if s[0] == s[1] or s[1] == s[2] or s[2] == s[3]:
        return False
    return True


def check_valid_20(s):
    if s[0] == s[2] or s[1] == s[3]:
        return False
    return True


def check_valid_21(s):
    if s[0] == s[3]:
        return False
    return True


def check_valid_22(s):
    if s[0] == s[1] or s[1] == s[2] or s[2] == s[3]:
        return False
    return True


def check_valid_23(s):
    if s[0] == s[2] or s[1] == s[3]:
        return False
    return True


def check_valid_24(s):
    if s[0] == s[3]:
        return False
    return True


def check_valid_25(s):
    if s[0] == s[1] or s[1] == s[2] or s[2] == s[3]:
        return False
    return True


def check_valid_26(s):
    if s[0] == s[2] or s[1] == s[3]:
        return False
    return True


def check_valid_27(s):
    if s[0] == s[3]:
        return False
    return True


def check_valid_28(s):
    if s[0] == s[1] or s[1] == s[2] or s[2] == s[3]:
        return False
    return True


def check_valid_29(s):
    if s[0] == s[2] or s[1] == s[3]:
        return False
    return True


def check_valid_30(s):
    if s[0] == s[3]:
        return False
    return True


def check_valid_31(s):
    if s[0] == s[1] or s[1] == s[2] or s[2] == s[3]:
        return False
    return True


def check_valid_32(s):
    if s[0] == s[2] or s[1] == s[3]:
        return False
    return True


def check_valid_33(s):
    if s[0] == s[3]:
        return False
    return True


def check_valid_34(s):
    if s[0] == s[1] or s[1] == s[2] or s[2] ==
