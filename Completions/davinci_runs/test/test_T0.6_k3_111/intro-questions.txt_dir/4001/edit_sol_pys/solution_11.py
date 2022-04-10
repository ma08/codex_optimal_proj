
def main():
    """main function"""
    num = int(input())
    num_list1 = list(map(int, input().split()))
    num_list1.sort()
    num_list1 = list(set(num_list1)) # remove duplicate numbers
    num_list1.sort() # sort again
    num_list2 = [] # list of duplicate numbers
    num_list3 = [] # list of unique numbers
    for i in range(len(num_list1)):
        if num_list1[i] == num_list1[i-1]:
            num_list2.append(num_list1[i])
        else:
            num_list3.append(num_list1[i])
    num_list3.sort()
    print(num_list3[0]*num_list2[0], end=" ")
    for i in range(1, len(num_list3)):
        print(num_list3[i], end=" ")
    for i in range(1, len(num_list2)):
        print(num_list2[i], end=" ")

if __name__ == '__main__':
    main()
