

def main():
    n = int(input())
    a_list = list(map(int, input().split()))

    a_list.sort()
    print(a_list[-1] - a_list[0])

if __name__ == '__main__':
    main()
