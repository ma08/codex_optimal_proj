

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    # print(n, m, a)
    
    # create a list of tuples (a[i], i)
    a_i = []
    for i in range(n):
        a_i.append((a[i], i))
    # print(a_i)
    
    # sort the list of tuples
    a_i.sort()
    # print(a_i)
    
    # create a list of tuples (a[i], i, a[i] - m)
    a_i_m = []
    for i in range(n):
        a_i_m.append((a[i], i, a[i] - m))
    # print(a_i_m)
    
    # sort the list of tuples
    a_i_m.sort()
    # print(a_i_m)
    
    # create a list of tuples (a[i], i, a[i] - m, a[i] - m + 1)
    a_i_m_1 = []
    for i in range(n):
        a_i_m_1.append((a[i], i, a[i] - m, a[i] - m + 1))
    # print(a_i_m_1)
    
    # sort the list of tuples
    a_i_m_1.sort()
    # print(a_i_m_1)
    
    # create a list of tuples (a[i], i, a[i] - m, a[i] - m + 1, a[i] - m - 1)
    a_i_m_1_m1 = []
    for i in range(n):
        a_i_m_1_m1.append((a[i], i, a[i] - m, a[i] - m + 1, a[i] - m - 1))
    # print(a_i_m_1_m1)
    
    # sort the list of tuples
    a_i_m_1_m1.sort()
    # print(a_i_m_1_m1)
    
    # create a list of tuples (a[i], i, a[i] - m, a[i] - m + 1, a[i] - m - 1, a[i] - m + 2)
    a_i_m_1_m1_2 = []
    for i in range(n):
        a_i_m_1_m1_2.append((a[i], i, a[i] - m, a[i] - m + 1, a[i] - m - 1, a[i] - m + 2))
    # print(a_i_m_1_m1_2)
    
    # sort the list of tuples
    a_i_m_1_m1_2.sort()
    # print(a_i_m_1_m1_2)
    
    # create a list of tuples (a[i], i, a[i] - m, a[i] - m + 1, a[i] - m - 1, a[i] - m + 2, a[i] - m - 2)
    a_i_m_1_m1_2_m2 = []
    for i in range(n):
        a_i_m_1_m1_2_m2.append((a[i], i, a[i] - m, a[i] - m + 1, a[i] - m - 1, a[i] - m + 2, a[i] - m - 2))
    # print(a_i_m_1_m1_2_m2)
    
    # sort the list of tuples
    a_i_m_1_m1_2_m2.sort()
    # print(a_i_m_1_m1_2_m2)
    
    # count the pairs
    count = 0
    for i in range(n):
        if a[i] == m:
            count += 1
    
    # m < a[i]
    for i in range(n):
        # m + 1 < a[i]
        if a[i] - m > 1:
            # find the number of elements greater than a[i] - m - 1
            count += i - a_i_m_1_m1_2_m2.index(a[i] - m - 1, i)
        # m + 1 = a[i]
        elif a[i] - m == 1:
            # find the number of elements greater than a[i] - m - 1
            count += i - a_i_m_1_m1_2.index(a[i] - m - 1, i)
    # m > a[i]
    for i in range(n):
        # m - 1 > a[i]
        if a[i] - m < -1:
            # find the number of elements less than a[i] - m + 1
            count += a_i_m_1_m1_2_m2.index(a[i] - m + 1, i) - i
        # m - 1 = a[i]
        elif a[i] - m == -1:
            # find the number of elements less than a[i] - m + 1
            count += a_i_m_1_m1_2.index(a[i] - m + 1, i) - i
    
    print(count)
    
    
if __name__ == '__main__':
    main()