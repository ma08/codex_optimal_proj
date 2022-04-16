

def get_input(input_func=input):
    t = int(input())
    for i in range(t):
        n = int(input_func())
        yield n

def solve(n):
    pass

if __name__ == '__main__':
    for n in get_input():
        print(solve(n))
