
def nextPermutation(a):
    i = len(a) - 1
    while i > 0 and a[i - 1] >= a[i]:
        i -= 1
    if i <= 0:
        return False

    j = len(a) - 1
    while a[j] <= a[i - 1]:
        j -= 1
    a[i - 1], a[j] = a[j], a[i - 1]

    a[i:] = reversed(a[i:])
    return True

def main():
    # Read input
    x = input()

    # Convert to int array and sort
    x_arr = [int(c) for c in str(x)]
    x_arr.sort()

    # Find next permutation

    # Find next permutation
    if nextPermutation(x_arr):
        print(int(''.join(map(str, x_arr)))) # Convert back to int
    else:
        print(0)

if __name__ == "__main__":
    main()
