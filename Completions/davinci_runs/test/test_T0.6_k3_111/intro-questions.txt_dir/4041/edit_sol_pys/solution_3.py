

def solve_easy(n, m):
    return n - m

def solve_hard(n, m):
    pass

if __name__ == "__main__":
    n = int(input())
    m = int(input())
    
    if len(n) <= 200 and len(m) <= 200:
        print(solve_easy(n, m))
    else:
        print(solve_hard(n, m))
