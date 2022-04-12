

#The following is the solution to the problem: https://open.kattis.com/problems/filefragmentation

n = int(input())

for i in range(n):
    file_name, file_size, num_fragments = input().split()
    file_size = int(file_size)
    num_fragments = int(num_fragments)
    fragments = list(map(int, input().split()))
    fragments.sort()
    sum_fragments = sum(fragments)
    if (sum_fragments > file_size):
        print("{} {}".format(file_name, "INCONSISTENT"))
    else:
        print("{} {}".format(file_name, file_size - sum_fragments))
