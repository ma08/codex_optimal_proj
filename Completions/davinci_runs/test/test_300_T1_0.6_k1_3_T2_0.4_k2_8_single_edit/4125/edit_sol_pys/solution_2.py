

def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    a_list.sort()
    if a_list[0] == a_list[-1]:
        print(n // 2)
    else:
        print(n - a_list.count(a_list[-1]))

if __name__ == '__main__':
    main()
