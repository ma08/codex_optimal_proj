

def next_permutation(arr):
    i = len(arr) - 1
    while i > 0 and arr[i - 1] >= arr[i]:
        i = i - 1
    if i == 0:
        return False

    j = len(arr) - 1
    while arr[j] <= arr[i - 1]:
        j = j - 1
    arr[i - 1], arr[j] = arr[j], arr[i - 1]

    arr[i:] = reversed(arr[i:])
    return True

def main():
    # Read input
    x = input()

    # Convert to int array
    x_arr = [int(c) for c in x]

    # Find next permutation
    if next_permutation(x_arr):
        print(''.join(map(str, x_arr)))
    else:
        print(0)

if __name__ == "__main__":
    main() 
