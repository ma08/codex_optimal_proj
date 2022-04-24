

def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    a_list.sort()
    a_list = a_list[::-1]
    alice = sum(a_list[::2])
    bob = sum(a_list[1::2])
    print(alice - bob)

if __name__ == '__main__':
    main()
