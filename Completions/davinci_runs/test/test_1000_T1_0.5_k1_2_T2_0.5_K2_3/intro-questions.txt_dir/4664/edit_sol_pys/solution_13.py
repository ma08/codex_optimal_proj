

# Enter your code here. Read input from STDIN. Print output to STDOUT
m = int(raw_input())
m_list = set(map(int, raw_input().split()))
n = int(raw_input())
n_list = set(map(int, raw_input().split()))
print(len(m_list.union(n_list)))
