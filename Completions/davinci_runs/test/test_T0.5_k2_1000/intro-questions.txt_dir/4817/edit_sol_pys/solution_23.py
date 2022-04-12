

def next_permutation(a)
    n = len(a) # get the length of the array
    i = n - 1
    while i > 0 and a[i-1] >= a[i]: # find the first index where a[i-1] < a[i]
        i -= 1
    if i <= 0: # if not found, then the array is in descending order
        return False
    j = n - 1
    while a[j] <= a[i-1]: # find the last index where a[j] > a[i-1]
        j -= 1
    a[i-1], a[j] = a[j], a[i-1] # swap a[i-1] and a[j]
    a[i:] = reversed(a[i:]) # reverse the array from a[i] to the end
    return True

def main():
    s = input()
    a = [int(x) for x in s]
    if next_permutation(a):
        print(''.join([str(x) for x in a]))
    else:
        print(0)

if __name__ == "__main__":
    main()
