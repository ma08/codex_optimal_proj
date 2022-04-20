

def isGood(a):
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            if a[i] + a[j] in powers:
                return True
    return False

def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    if isGood(a):
        print(0)
        return
    for i in range(n):
        if isGood(a[:i]+a[i+1:]):
            print(1)
            return
    print(n)

powers = set()
for i in range(32):
    powers.add(2**i)

main()