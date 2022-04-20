

def main():
    """
    We need to find the number of pairs of numbers that are divisible by k
    when concatenated.
    """
    n, k = map(int, input().split())
    nums = map(int, input().split())

    # Map each number to its remainder when divided by k
    rems = {}
    for num in nums:
        rem = num % k
        if rem not in rems:
            rems[rem] = 0
        rems[rem] += 1

    # Count the number of pairs that are divisible by k
    count = 0
    for rem in rems:
        count += ((rems[rem] * (rems[rem] - 1)) // 2)

    # Count the number of pairs with the same remainder
    if 0 in rems:
        count += ((rems[0] * (rems[0] - 1)) // 2)

    for i in range(1, k):
        if i in rems and (k - i) in rems:
            count += (rems[i] * rems[k - i])

    print(count)

if __name__ == '__main__':
    main()