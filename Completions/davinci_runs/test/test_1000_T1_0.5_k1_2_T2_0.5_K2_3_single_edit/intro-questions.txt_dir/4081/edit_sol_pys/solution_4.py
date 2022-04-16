
import sys

def main():
    n = int(input())
    a = [int(x) for x in input().split()] #a = [1, 2, 3, 4, 5]
    assert len(a) == n #assert is a statement that evaluates a boolean expression.
    #If the boolean expression is true, it returns nothing and if it is false, it raises an AssertionError exception

    left = [0] * n #left = [0, 0, 0, 0, 0]
    right = [0] * n #right = [0, 0, 0, 0, 0]

    left[0] = 1 #left = [1, 0, 0, 0, 0]
    right[n-1] = 1

    for i in range(1, n):
        left[i] = left[i-1] #left = [1, 1, 0, 0, 0]
        if a[i] > a[i-1]:
            left[i] += 1 #left = [1, 1, 2, 0, 0]

    for i in range(n-2, -1, -1): #range(start, stop, step)
        right[i] = right[i+1]
        if a[i] < a[i+1]:
            right[i] += 1

    max_len = 0 #max_len = 0
    max_len_idx = -1
    for i in range(n): #i = 0, 1, 2, 3, 4
        if left[i] + right[i] > max_len:
            max_len = left[i] + right[i] #max_len = 2
            max_len_idx = i

    print(max_len) #print 2
    seq = []
    for i in range(max_len_idx, -1, -1): #i = 1
        if left[i] == 1:
            break
        seq.append('L')

    for i in range(max_len_idx, n): #i = 1, 2, 3, 4
        if right[i] == 1:
            break
        seq.append('R')

    print(''.join(seq)) #print LL

if __name__ == '__main__':
    main()
