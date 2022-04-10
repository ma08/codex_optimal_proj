

# from statistics import mode
import sys, math

# def find_mode(list):
#     try:
#         return mode(list)
#     except:
#         return 1

def find_mode(list):
    num_dict = {}
    for num in list:
        if num in num_dict:
            num_dict[num] += 1
        else:
            num_dict[num] = 1
    return max(num_dict, key=lambda key: num_dict[key]) if num_dict else 1

def find_median(list):
    list.sort()
    return list[int(math.floor(len(list) / 2))] if list else 1

# def find_median(list):
#     return sorted(list)[int(math.floor(len(list) / 2))]

def find_mean(list):
    return int(sum(list) / len(list)) if list else 1

def main():
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    print(find_mode(a) + find_median(a) + find_mean(a))

if __name__ == '__main__':
    main()


"""
# DO NOT READ THIS.

# I'm just writing down my thoughts during the problem-solving process

# The problem is asking for the sum of the mode, median and mean of the input.
# It's the same as finding the mode.
# Then the median + mean of the mode

# I think that the mode is the most frequent number in the list
# Maybe use a hash table?
# Maybe I can just sort it and find the most frequent number

# I think that the median is the middle number in the list
# I think that the mean is the average of the list

# I think that I can just use the statistics module to find this
# But that's cheating
# I should try to solve it on my own

# I think that I can just sort the list and find the number that repeats the most
# But what if there are no repeated numbers?
# I guess I can just return 1

# I think that I can just sort the list and find the middle number
# I can just use the floor of the length of the list divided by 2

# I think that I can just find the sum of the list and divide it by the length of the list
# I think that I should use floor division
"""
