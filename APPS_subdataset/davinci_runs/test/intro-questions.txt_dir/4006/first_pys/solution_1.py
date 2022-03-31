

def f(n):
    while(n % 10 == 0):
        n /= 10
    return n + 1

def main():
    n = int(input())
    reachable = set()
    reachable.add(n)
    while(True):
        n = f(n)
        if(n in reachable):
            break
        reachable.add(n)
    print(len(reachable))

main()