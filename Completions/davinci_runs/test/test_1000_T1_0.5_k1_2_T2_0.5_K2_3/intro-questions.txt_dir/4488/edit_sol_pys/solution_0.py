

def compare_numbers(A, B):
    if A > B:
        return ">";
    elif A < B:
        return "<";
    else:
        return "=";

A = input()
B = input()
print(compare_numbers(A, B))
