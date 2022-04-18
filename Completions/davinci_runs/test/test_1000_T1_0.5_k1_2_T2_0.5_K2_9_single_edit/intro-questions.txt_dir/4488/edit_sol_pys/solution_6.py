

def compare_numbers(a,b):
    if len(a) > len(b):
        return "greater"
    elif len(a) < len(b):
        return "less"
    for i in range(len(a)):
        if int(a[i]) > int(b[i]):
            return "greater"
        elif int(a[i]) < int(b[i]):
            return "less"
    return "equal"

a = input()
b = input()
print(compare_numbers(a,b))
