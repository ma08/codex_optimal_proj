

#!/usr/bin/python
import sys
import os
import math

def get_max_cluster_size(cluster_size_list):
    max_size = 0
    for i in cluster_size_list:
        if i > max_size:
            max_size = i
    return max_size

def get_max_cluster_size_index(cluster_size_list):
    max_size = get_max_cluster_size(cluster_size_list)
    for i in range(len(cluster_size_list)):
        if cluster_size_list[i] == max_size:
            return i

def get_max_cluster_size_index_list(cluster_size_list):
    max_size = get_max_cluster_size(cluster_size_list)
    max_size_index_list = []
    for i in range(len(cluster_size_list)):
        if cluster_size_list[i] == max_size:
            max_size_index_list.append(i)
    return max_size_index_list

def get_min_cluster_size(cluster_size_list):
    min_size = sys.maxsize
    for i in cluster_size_list:
        if i < min_size:
            min_size = i
    return min_size

def get_min_cluster_size_index(cluster_size_list):
    min_size = get_min_cluster_size(cluster_size_list)
    for i in range(len(cluster_size_list)):
        if cluster_size_list[i] == min_size:
            return i

def get_min_cluster_size_index_list(cluster_size_list):
    min_size = get_min_cluster_size(cluster_size_list)
    min_size_index_list = []
    for i in range(len(cluster_size_list)):
        if cluster_size_list[i] == min_size:
            min_size_index_list.append(i)
    return min_size_index_list

def get_cluster_size(cluster_list, cluster_size_list, cluster_size_list_len, cluster_size_list_max_size, cluster_size_list_min_size):
    for i in range(len(cluster_size_list_len)):
        cluster_size_list[i] = 0
    for i in range(len(cluster_list)):
        cluster_size_list[cluster_list[i]] += 1
    cluster_size_list_max_size = get_max_cluster_size(cluster_size_list)
    cluster_size_list_min_size = get_min_cluster_size(cluster_size_list)

def merge_cluster(cluster_list, cluster_size_list, cluster_size_list_len, cluster_size_list_max_size, cluster_size_list_min_size, cluster_size_list_max_size_index, cluster_size_list_min_size_index):
    max_size_index_list = get_max_cluster_size_index_list(cluster_size_list)
    min_size_index_list = get_min_cluster_size_index_list(cluster_size_list)
    max_size_index = max_size_index_list[0]
    min_size_index = min_size_index_list[0]
    for i in range(len(cluster_list)):
        if cluster_list[i] == max_size_index:
            cluster_list[i] = min_size_index
    cluster_size_list[min_size_index] += cluster_size_list[max_size_index]
    cluster_size_list[max_size_index] = 0
    cluster_size_list_len -= 1
    cluster_size_list_max_size = get_max_cluster_size(cluster_size_list)
    cluster_size_list_min_size = get_min_cluster_size(cluster_size_list)

def is_cluster_equal_to_k(cluster_size_list, cluster_size_list_max_size, k):
    if cluster_size_list_max_size > k:
        return True
    else:
        return False

def get_cluster_number(cluster_size_list, cluster_size_list_len):
    cluster_number = 0
    for i in range(len(cluster_size_list)):
        if cluster_size_list[i] > 0:
            cluster_number += 1
    return cluster_number

def get_cluster_list(cluster_size_list, cluster_size_list_len):
    cluster_list = []
    for i in range(len(cluster_size_list)):
        if cluster_size_list[i] > 0:
            cluster_list.append(i)
    return cluster_list

def get_cluster_size_list(cluster_list, cluster_size_list, cluster_size_list_len, cluster_size_list_max_size, cluster_size_list_min_size):
    for i in range(len(cluster_size_list)):
        cluster_size_list[i] = 0
    for i in range(len(cluster_list)):
        cluster_size_list[cluster_list[i]] += 1

def main():
    n, k = map(int, input().split())
    n_min_1 = n-1
    cluster_list = []
    cluster_size_list = []
    cluster_size_list_len = 0
    cluster_size_list_max_size = 0
    cluster_size_list_min_size = 0
    for i in range(n_min_1):
        cluster_list.append(i)
        cluster_size_list.append(0)
    cluster_size_list_len = n_min_1
    get_cluster_size(cluster_list, cluster_size_list, cluster_size_list_len, cluster_size_list_max_size, cluster_size_list_min_size)
    while is_cluster_equal_to_k(cluster_size_list, cluster_size_list_max_size, k) == True:
        merge_cluster(cluster_list, cluster_size_list, cluster_size_list_len, cluster_size_list_max_size, cluster_size_list_min_size, cluster_size_list_max_size_index, cluster_size_list_min_size_index)
    cluster_number = get_cluster_number(cluster_size_list, cluster_size_list_len)
    cluster_list = get_cluster_list(cluster_size_list, cluster_size_list_len)
    cluster_size_list = get_cluster_size_list(cluster_list, cluster_size_list, cluster_size_list_len, cluster_size_list_max_size, cluster_size_list_min_size)
    print(cluster_number)
    for i in range(n_min_1):
        print(cluster_list[cluster_list[i]]+1, end=" ")
    print()
    """
    for i in range(len(cluster_list)):
        cluster_list[i] = 0
    for i in range(len(cluster_size_list)):
        cluster_size_list[i] = 0
    for i in range(n_min_1):
        cluster_list.append(0)
        cluster_size_list.append(0)
    cluster_size_list_len = n_min_1
    get_cluster_size(cluster_list, cluster_size_list, cluster_size_list_len, cluster_size_list_max_size, cluster_size_list_min_size)
    while is_cluster_equal_to_k(cluster_size_list, cluster_size_list_max_size, k) == True:
        merge_cluster(cluster_list, cluster_size_list, cluster_size_list_len, cluster_size_list_max_size, cluster_size_list_min_size, cluster_size_list_max_size_index, cluster_size_list_min_size_index)
    cluster_number = get_cluster_number(cluster_size_list, cluster_size_list_len)
    cluster_list = get_cluster_list(cluster_size_list, cluster_size_list_len)
    cluster_size_list = get_cluster_size_list(cluster_list, cluster_size_list, cluster_size_list_len, cluster_size_list_max_size, cluster_size_list_min_size)
    print(cluster_number)
    for i in range(n_min_1):
        print(cluster_list[cluster_list[i]]+1, end=" ")
    print()
    """

if __name__ == '__main__':
    main()