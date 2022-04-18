

import sys

def main():
    k = int(sys.stdin.readline())
    if k == 1:
        print("0 1")
    else:
        A = [0, 1]
        B = [1, 1]
        for i in range(2, k+1):
            A.append(B[i-1])
            B.append(A[i-1] + B[i-1])
        print(str(A[k]) + " " + str(B[k]))

if __name__ == '__main__':
    main()
