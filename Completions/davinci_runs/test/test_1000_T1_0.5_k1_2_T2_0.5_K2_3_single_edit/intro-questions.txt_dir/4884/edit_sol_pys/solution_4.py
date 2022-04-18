

def carrots(n, p):
    carrots = p
    for i in range(n):
        input() # ignore all the names
    print(carrots) # print the number of carrots

n, p = map(int, input().split())
carrots(n, p)
