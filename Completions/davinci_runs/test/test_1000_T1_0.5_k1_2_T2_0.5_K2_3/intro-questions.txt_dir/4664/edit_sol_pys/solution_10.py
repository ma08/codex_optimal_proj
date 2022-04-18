
# Enter your code here. Read input from STDIN. Print output to STDOUT
m = raw_input()
m_list = set(raw_input().split())
n = raw_input()
n_list = set(raw_input().split())
print len(m_list.union(n_list))
