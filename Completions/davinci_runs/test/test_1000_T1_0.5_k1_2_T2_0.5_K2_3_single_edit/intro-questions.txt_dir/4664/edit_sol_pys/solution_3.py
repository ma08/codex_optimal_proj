

# Enter your code here. Read input from STDIN. Print output to STDOUT 

# # set1 = {1, 2, 3, 4, 5}
# # set2 = {3, 4, 5, 6, 7}

# # print set1.difference(set2)
# # print set2.difference(set1)

# # print set1.symmetric_difference(set2)

# m = raw_input()
# m_list = raw_input().split()
# n = raw_input()
# n_list = raw_input().split()

# set1 = set(m_list)
# set2 = set(n_list)

# sym_diff = set1.symmetric_difference(set2)

# for i in sorted(sym_diff):
#     print i

# Create a set
set1 = set(["a", "b"])
set2 = set(["c", "d"])

# Add element to set
set1.add("e")

# Remove element from set
set1.remove("a")

# Update set
set1.update(set2)

# Get length of set
print len(set1)
