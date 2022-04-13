
def main():
    n = int(input())
    a = sorted([int(item) for item in input().split()], reverse=True)
    alice_sum = 0
    bob_sum = 0
    for i in range(n):
        if i % 2 == 0:
            alice_sum += a[i]
        else:
            bob_sum += a[i]
    print(alice_sum, bob_sum)


main()
