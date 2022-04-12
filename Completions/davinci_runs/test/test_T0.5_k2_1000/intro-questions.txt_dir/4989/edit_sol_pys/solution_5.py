

def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    a.sort(reverse=True)
    alice = 0
    bob = 0
    for i in range(n):
        if i % 2 == 0:
            alice += a[i]
        else:
            bob += a[i]
    print(alice, bob)

main()
