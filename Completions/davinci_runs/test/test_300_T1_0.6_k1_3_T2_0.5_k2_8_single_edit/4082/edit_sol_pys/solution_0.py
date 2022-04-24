
def max_increasing_subarray(a):
    max_length = 0
    length = 0
    for i in range(1,len(a)):
        if a[i] > a[i-1]:
            length += 1
        else:
            if length > max_length:
                max_length = length
            length = 0
    return max_length+1
