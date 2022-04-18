

# Split the input into string and queries
def split_input(input):
    input_split = input.splitlines()
    n_q = input_split[0].split()
    n = int(n_q[0])
    q = int(n_q[1])
    string = input_split[1]
    queries = []
    for i in range(q):
        queries.append(input_split[2 + i].split())
    return n, q, string, queries

# Given a string s and a substring sub, returns the number of times sub occurs in s
def count_substring(string, sub):
    count = start = 0
    while True:
        start = string.find(sub, start) + 1
        if start > 0:
            count+=1
        else:
            return count

# Given a string s and a substring sub, returns the number of times sub occurs in s
# as a substring
def count_substring_substring(string, sub):
    count = 0
    for i in range(len(string) - 1):
        if sub in string[i:i+2]:
            count+=1
    return count

# Counts the number of times AC occurs in the substring of S starting at index l_i and ending at index r_i
def count_ac(string, l, r):
    substring = string[l-1:r]
    return count_substring_substring(substring, 'AC')

# Prints the number of times AC occurs in the substring of S starting at index l_i and ending at index r_i for each query
def solve(input):
    n, q, string, queries = split_input(input)
    for query in queries:
        l = int(query[0])
        r = int(query[1])
        print(count_ac(string, l, r))

# Read input from stdin
if __name__ == '__main__':
    input = sys.stdin.read()
    solve(input)
