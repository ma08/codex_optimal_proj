

# Split the input into string and queries
def split_input(input):
    n, q = map(int, input.split())
    string = input.split()[1]
    queries = []
    for i in range(2, q + 2):
        queries.append(input.split()[i].split())
    return n, q, string, queries

# Given a string s and a substring sub, returns the number of times sub occurs in s
def count_substring(s, sub):
    for i in range(len(s) - len(sub) + 1):
        if s[i:i + len(sub)] == sub:
            count += 1
    return count

# Given a string s and a substring sub, returns the number of times sub occurs in s
# as a substring
def count_substring_substring(s, sub):
    count = 0
    for i in range(len(s) - len(sub) + 1):
        if sub in s[i:i + len(sub)]:
            count += 1
    return count

# Counts the number of times AC occurs in the substring of string starting at index l and ending at index r
def count_ac(string, l, r):
    substring = string[l - 1:r]
    return count_substring_substring(substring, 'AC')

# Prints the number of times AC occurs in the substring of string starting at index l and ending at index r for each query
def solve(input):
    _, _, string, queries = split_input(input)
    for query in queries:
        l = int(query[0])
        r = int(query[1])
        print(count_ac(string, l, r))

# Read input from stdin
if __name__ == '__main__':
    input = sys.stdin.read()
    solve(input)
