
def remove_adjacent(nums):
    i = 0
    while i < len(nums) - 1:
        if nums[i] == nums[i + 1]:
            nums = nums[:i + 1] + nums[i + 2:]
        else:
            i += 1
    return nums
def linear_merge(list1, list2):
    list1 = remove_adjacent(list1)
    list2 = remove_adjacent(list2)
    list3 = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            list3.append(list1[i])
            i += 1
        elif list1[i] > list2[j]:
            list3.append(list2[j])
            j += 1
        else:
            list3.append(list1[i])
            list3.append(list2[j])
            i += 1
            j += 1
    if i < len(list1):
        list3.extend(list1[i:])
    else:
        list3.extend(list2[j:])
    return list3
