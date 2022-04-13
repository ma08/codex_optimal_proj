#solution

def get_input():
    s,t = input().split()
    a,b = map(int,input().split())
    u = input()
    return s,t,a,b,u

def solve(s,t,a,b,u):
    if s == u:
        print(a-1,b)
    else:
        print(a,b-1)

s,t,a,b,u = get_input()
solve(s,t,a,b,u)
