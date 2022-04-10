
def main():
    """main function"""
    num = int(input())
    num_list = list(map(int, input().split()))
    num_list.sort()
    num_list = list(set(num_list))
    num_list.sort()
    num_list_dup = [] # list of duplicate numbers
    num_list_uniq = [] # list of unique numbers
    for i in range(len(num_list)):
        if num_list[i] == num_list[i-1]:
            num_list_dup.append(num_list[i])
        elif num_list[i] != num_list[i-1]:
            num_list_uniq.append(num_list[i])
    num_list_uniq.sort()
    print(num_list_uniq[0]*num_list_dup[0], end=" ")
    for i in range(1, len(num_list_uniq)):
        print(num_list_uniq[i], end=" ")
    for i in range(1, len(num_list_dup)):
        print(num_list_dup[i], end=" ")

if __name__ == '__main__':
    main()
