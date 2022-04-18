

def get_min_difference(n):
    min_diff = 1001
    for i in range(len(n) - 2):
        diff = abs(753 - int(n[i:i+3]))
        if diff < min_diff:
            min_diff = diff
    return min_diff

if __name__ == '__main__':
    n = input()
    print(get_min_difference(n))
