
def find_max_sum_subarray(arr):
    # [1, 2, 3, -4, 5]
    # [1, 2, 3, -4, 5, -2, 3]
    # [1, 2, 3, -4, 5, -2, 3, -1]
    # [1, 2, 3, -4, 5, -2, 3, -1, 4]
    # [1, 2, 3, -4, 5, -2, 3, -1, 4, -5]
    # [1, 2, 3, -4, 5, -2, 3, -1, 4, -5, 6]
    # [1, 2, 3, -4, 5, -2, 3, -1, 4, -5, 6, -7]
    # [1, 2, 3, -4, 5, -2, 3, -1, 4, -5, 6, -7, 8]
    # [1, 2, 3, -4, 5, -2, 3, -1, 4, -5, 6, -7, 8, -9]
    # [1, 2, 3, -4, 5, -2, 3, -1, 4, -5, 6, -7, 8, -9, 10]
    # [1, 2, 3, -4, 5, -2, 3, -1, 4, -5, 6, -7, 8, -9, 10, -11]
    # [1, 2, 3, -4, 5, -2, 3, -1, 4, -5, 6, -7, 8, -9, 10, -11, 12]
    # [1, 2, 3, -4, 5, -2, 3, -1, 4, -5, 6, -7, 8, -9, 10, -11, 12, -13]
    # [1, 2, 3, -4, 5, -2, 3, -1, 4, -5, 6, -7, 8, -9, 10, -11, 12, -13, 14]
    # [1, 2, 3, -4, 5, -2, 3, -1, 4, -5, 6, -7, 8, -9, 10, -11, 12, -13, 14, -15]
    # [1, 2, 3, -4, 5, -2, 3, -1, 4, -5, 6, -7, 8, -9, 10, -11, 12, -13, 14, -15, 16]
    # [1, 2, 3, -4, 5, -2, 3, -1, 4, -5, 6, -7, 8, -9, 10, -11, 12, -13, 14, -15, 16, -17]
    # [1, 2, 3, -4, 5, -2, 3, -1, 4, -5, 6, -7, 8, -9, 10, -11, 12, -13, 14, -15, 16, -17, 18]
    # [1, 2, 3, -4, 5, -2, 3, -1, 4, -5, 6, -7, 8, -9, 10, -11, 12, -13, 14, -15, 16, -17, 18, -19]
    # [1, 2, 3, -4, 5, -2, 3, -1, 4, -5, 6, -7, 8, -9, 10, -11, 12, -13, 14, -15, 16, -17, 18, -19, 20]
    # [1, 2, 3, -4, 5, -2, 3, -1, 4, -5, 6, -7, 8, -9, 10, -11, 12, -13, 14, -15, 16, -17, 18, -19, 20, -21]
    # [1, 2, 3, -4, 5, -2, 3, -1, 4, -5, 6, -7, 8, -9, 10, -11, 12, -13, 14, -15, 16, -17, 18, -19, 20, -21, 22]
    # [1, 2, 3, -4, 5, -2, 3, -1, 4, -5, 6, -7, 8, -9, 10, -11, 12, -13, 14, -15, 16, -17, 18, -19, 20, -21, 22, -23]
    # [1, 2, 3, -4, 5, -2, 3, -1, 4, -5, 6, -7, 8, -9, 10, -11, 12, -13, 14, -15, 16, -17, 18, -19, 20, -21, 22, -23, 24]
    # [1, 2, 3, -4, 5, -2, 3, -1, 4, -5, 6, -7, 8, -9, 10, -11, 12, -13, 14, -15, 16, -17, 18, -19, 20, -21, 22, -23, 24, -25]
    # [1, 2, 3, -4, 5, -2, 3, -1, 4, -5, 6, -7, 8, -9, 10, -11, 12, -13, 14, -15, 16, -17, 18, -19, 20, -21, 22, -23, 24, -25, 26]
    # [1, 2, 3, -4, 5, -2, 3, -1, 4, -5, 6, -7, 8, -9, 10, -11, 12, -13, 14, -15, 16, -17, 18, -19, 20, -21, 22, -23, 24, -25, 26, -27]
    arr.sort()
    return arr[-1] * arr[-2] * arr[-3]
