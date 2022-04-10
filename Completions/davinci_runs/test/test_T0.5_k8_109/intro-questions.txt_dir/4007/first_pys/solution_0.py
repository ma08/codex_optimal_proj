

def main():
    """ Main """
    n = int(input())
    f_i = [int(i) for i in input().split()]
    # print(n, f_i)

    for i in range(1, n+1):
        if i not in f_i:
            for j in range(n):
                if f_i[j] == 0:
                    f_i[j] = i
                    break
    # print(f_i)
    for i in f_i:
        print(i, end=" ")

main()