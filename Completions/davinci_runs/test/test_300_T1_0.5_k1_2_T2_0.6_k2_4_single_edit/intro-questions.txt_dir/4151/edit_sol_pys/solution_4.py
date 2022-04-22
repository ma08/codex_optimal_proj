import sys
import math

def main():
    n = int(sys.stdin.readline().strip())
    a = list(map(int, sys.stdin.readline().strip().split()))
    assert 2 <= n <= 2 * 10**5
    assert len(a) == n
    assert all(1 <= x <= 10**9 for x in a)
    a.sort()
    if a[0] == a[1]:
        print(a[0]*a[1])
        return
    else:
        max_num = a[-1]*a[-2]
        max_index = n-1
        min_index = n-2
        if max_num > a[0]*a[1]:
            print(max_num)
            return
        else:
            for i in range(n-3, -1, -1):
                if a[i]*a[i+1] > max_num:
                    max_num = a[i]*a[i+1]
                    max_index = i
            if a[0]*a[1] > max_num:
                print(a[0]*a[1])
                return
            else:
                for i in range(n-3, -1, -1):
                    if a[i]*a[i+1] < max_num:
                        min_index = i
                        break
                print(max_num*a[min_index])
                return
    # TODO: solve the problem


if __name__ == '__main__':
    main()
