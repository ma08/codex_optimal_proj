
# Enter your code here. Read input from STDIN. Print output to STDOUT
m = raw_input()
m_list = raw_input().split()
n = raw_input()
n_list = raw_input().split()
set1 = set(m_list)
set2 = set(n_list)
sym_diff = set1.symmetric_difference(set2)

for i in sorted(sym_diff):
    print i
