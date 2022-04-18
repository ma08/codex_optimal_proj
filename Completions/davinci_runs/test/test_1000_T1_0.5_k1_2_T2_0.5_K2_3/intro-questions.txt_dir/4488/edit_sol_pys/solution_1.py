
def compare_numbers(a,b):
    if len(a) > len(b):
        return "GREATER"
    elif len(a) < len(b):
        return "LESS"
    else:
        if int(a) > int(b):
            return "GREATER"
        elif int(a) < int(b):
            return "LESS"
        else:
            return "EQUAL"

a = input()
b = input()
print(compare_numbers(a,b))
