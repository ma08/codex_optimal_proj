
import sys

def main():
    K = int(sys.stdin.readline())
    if K == 1:
        print("0 1")
    else:
        a = [0, 1]
        b = [1, 1]
        for i in range(2, k+1):
            a.append(b[i-1])
            b.append(a[i-1] + b[i-1])
        print(str(a[k]) + " " + str(b[k]))

if __name__ == '__main__':
    main()
