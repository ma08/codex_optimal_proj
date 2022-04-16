

def main():
    n = int(input())
    my_list = []
    for x in range(n):
        my_list.append(int(input()))

    for x in range(1, my_list[n-1]+1):
        if x not in my_list:
            print(x)


main()
