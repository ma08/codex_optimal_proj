def find_max_min(num_list):
    num_list.sort()
    if num_list[0] == num_list[-1]:
        return [len(num_list)]
    else:
        return [num_list[0], num_list[-1]]


print(find_max_min([1, 2, 3, 4]))
