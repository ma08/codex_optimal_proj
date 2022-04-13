

def compare_numbers(A, B):
    if len(A) > len(B):
        return "GREATER"
    elif len(A) < len(B):
        return "LESS"
    else:
        for i in range(len(A)-1):
            if int(A[i+1]) > int(B[i+1]):
                return "GREATER"
            elif int(A[i+1]) < int(B[i+1]):
                return "LESS"
        return "EQUAL"

A = input()
B = input()
print(compare_numbers(A, B))
