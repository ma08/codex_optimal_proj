
def main():
    """main function"""
    num = int(input())
    num_list = list(map(int, input().split()))
    num_list.sort()
    num_list = list(set(num_list))
    num_list.sort()
    num_list2 = []
    num_list3 = []
    for i in range(len(num_list)):
        if num_list[i] == num_list[i-1]:
            num_list2.append(num_list[i])
        else:
            num_list3.append(num_list[i])
    num_list3.sort()
    print(num_list3[0]*num_list2[0], end=" ")
    for i in range(1, len(num_list3)):
        print(num_list3[i], end=" ")
    for i in range(1, len(num_list2)):
        print(num_list2[i], end=" ")

if __name__ == '__main__':
    main()