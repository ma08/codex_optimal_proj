

def compare_numbers(A,B):
    if int(A) > int(B):
        return "GREATER"
    elif int(A) < int(B):
        return "LESS"
    else:
        return "EQUAL"

A = input()
B = input()
print(compare_numbers(A,B))
