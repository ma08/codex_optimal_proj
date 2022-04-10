

def solve_easy(a, b):
    return len(a) - len(b)

def solve_hard(a, b):
    return 0

if __name__ == "__main__":
    a = input()
    b = input()
    
    if len(a) <= 200 and len(b) <= 200:
        print(solve_easy(a, b))
    else:
        print(solve_hard(a, b))
