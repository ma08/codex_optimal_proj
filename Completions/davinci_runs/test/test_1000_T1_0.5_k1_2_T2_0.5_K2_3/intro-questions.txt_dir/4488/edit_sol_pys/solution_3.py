


def compare_numbers(a, b):
    if len(a) > len(b):
        return "GREATER"
    elif len(a) < len(b):
        return "LESS"
    else:
        for i in range(len(a)):
            if int(a[i]) > int(b[i]):
                return "GREATER"
            elif int(a[i]) < int(b[i]):
                return "LESS"
        return "EQUAL"

a = input()
b = input()
print(compare_numbers(a, b))
