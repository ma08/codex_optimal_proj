

def solve_easy(s, t):
    return len(s) - len(t)

def solve_hard(s, t):
    pass

if __name__ == "__main__":
    s = input()
    t = input()
    
    if len(s) <= 200 and len(t) <= 200:
        print(solve_easy(s, t))
    else:
        print(solve_hard(s, t))