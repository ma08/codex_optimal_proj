

# Enter your code here. Read input from STDIN. Print output to STDOUT

# set1 = {1, 2, 3, 4, 5}
# set2 = {3, 4, 5, 6, 7}

# print set1.difference(set2)
# print set2.difference(set1)

# print set1.symmetric_difference(set2)

m = int(raw_input())
m_list = map(int, raw_input().split())
n = int(raw_input())
n_list = map(int, raw_input().split())

set1 = set(m_list)
set2 = set(n_list)

sym_diff = set1.symmetric_difference(set2)

for i in sorted(sym_diff):
    print i
