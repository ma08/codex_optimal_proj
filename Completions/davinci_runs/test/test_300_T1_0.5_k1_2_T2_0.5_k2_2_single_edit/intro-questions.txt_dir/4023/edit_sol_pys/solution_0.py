import numpy as np

def main():
    n = int(input())
    a = np.array(list(map(int, input().split())))
    c = 0
    for i in range(n):
        if a[i] % 2 == 0:
            a[i] /= 2
        else:
            a[i] += 1
            c += 1
    print(c)

if __name__ == '__main__':
    main()
