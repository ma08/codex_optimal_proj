

def next_permutation(a): # следующая перестановка
    n = len(a)
    i = n - 1 # индекс первого элемента в последовательности спадания
    while i > 0 and a[i-1] >= a[i]:
        i -= 1
    if i <= 0:
        return False
    j = n - 1 # индекс первого элемента большего a[i-1]
    while a[j] <= a[i-1]:
        j -= 1
    a[i-1], a[j] = a[j], a[i-1]
    a[i:] = a[-1:i-1:-1]
    return True

def main():
    s = input()
    a = [int(x) for x in s] # список чисел
    if next_permutation(a):
        print(''.join([str(x) for x in a]))
    else:
        print(0)

if __name__ == "__main__":
    main()
