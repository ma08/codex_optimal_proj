

def next_permutation(a):
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

    # Convert to int array
    x_arr = [int(c) for c in str(x)]

    # Find next permutation
    if next_permutation(x_arr):
        print(int(''.join(map(str, x_arr))))
    else:
        print(0)

if __name__ == "__main__":
    main()