

def check_if_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i+1]:
            return False
    return True

def main():
    n = int(input().strip())
    arr = [int(x) for x in input().strip().split()]
    if check_if_sorted(arr):
        print('YES')
    else:
        print('NO')

if __name__ == '__main__':
    main()
