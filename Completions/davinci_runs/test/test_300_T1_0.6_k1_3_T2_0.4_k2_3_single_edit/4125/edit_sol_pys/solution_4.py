

def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    a_list.sort()
    m = a_list[-1] - a_list[0]
    for i in range(n):
        a_list[i] = a_list[i] - a_list[0]
    a_list[0] = 0
    for i in range(1, n):
        a_list[i] = a_list[i] + a_list[i - 1]
    for i in range(n):
        a_list[i] = a_list[i] * 2
    for i in range(n):
        a_list[i] = m - a_list[i]
    print(max(a_list))

if __name__ == '__main__':
    main()
