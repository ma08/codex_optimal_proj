

def f(n):
    while n % 10 == 0:
        n /= 10
    return n + 1

def main():
    n = int(input())
    reachable_set = set()
    reachable_set.add(n)
    while(True):
        n = f(n)
        if(n in reachable_set):
            break
        reachable_set.add(n)
    print(len(reachable_set))

main()
