
def main(arr):
    x = 0
    y = 0
    z = 0
    for i in range(len(arr)):
        if arr[i] == 0:
            x += 1
        elif arr[i] == 1:
            y += 1
        else:
            z += 1

    for i in range(x):
        print(0, end=' ')
    for i in range(y):
        print(1, end=' ')
    for i in range(z):
        print(2, end=' ')
    print()

main([0, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1])
