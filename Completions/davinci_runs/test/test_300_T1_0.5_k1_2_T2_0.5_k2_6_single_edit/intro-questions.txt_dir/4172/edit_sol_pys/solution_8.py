
def main(): 
    n = int(input())
    a = [int(x) for x in input().split()]
    s = set(a)
    if len(s) == n:
        print(n - 1)
    else:
        print(n)
main()
