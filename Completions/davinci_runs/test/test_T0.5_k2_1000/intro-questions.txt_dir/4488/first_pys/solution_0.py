

def compare_numbers(A,B):
    if len(A) > len(B):
        return "GREATER"
    elif len(A) < len(B):
        return "LESS"
    else:
        for i in range(len(A)):
            if int(A[i]) > int(B[i]):
                return "GREATER"
            elif int(A[i]) < int(B[i]):
                return "LESS"
        return "EQUAL"

A = input()
B = input()
print(compare_numbers(A,B))