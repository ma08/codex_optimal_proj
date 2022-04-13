

def main():
    """
    Sale order.
    """
    n = int(input())
    s_list = list(map(int, input().split()))
    if s_list[0] < sum(s_list[1:]):
        print("impossible")
    else:
        print("1", end=" ")
        for j in range(2, n+1):
            print(j, end=" ")

if __name__ == '__main__':
    main()
