

def main():
    n = int(input())
    a = sorted([int(i) for i in input().split()], reverse=True)
    alice = 0
    bob = 0
    for i in range(n):
        if i % 2 == 0:
            alice += a[i]
        else:
            bob += a[i]
    print(alice, bob)

main()
