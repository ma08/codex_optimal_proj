

def solve(a, b):
    if a < b:
        return a
    elif a > b:
        return b
    return a

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(solve(a, b))
