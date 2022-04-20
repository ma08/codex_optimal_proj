

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    answer = 0

    # Since we can only divide by 2, we take the highest element
    # and divide it by 2 until it's equal to the lowest element
    # or until it's less than the lowest element
    # Then, we do this again with the new highest value
    # This is the minimum number of operations
    while max(a) != min(a):
        highest = max(a)
        lowest = min(a)
        if highest % 2 == 1:
            highest -= 1
        highest //= 2
        if highest < lowest:
            highest = lowest
        a.append(highest)
        answer += 1

    print(answer)

main()