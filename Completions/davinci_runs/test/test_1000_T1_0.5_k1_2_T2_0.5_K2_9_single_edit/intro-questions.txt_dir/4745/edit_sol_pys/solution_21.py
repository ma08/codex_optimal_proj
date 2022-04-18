

n, k = map(int, input().split())
string = input()

# Put the string into a list
string_list = []
for i in string:
    string_list.append(i)

# Make a list of the numbers from 0 to n-1
index_list = []
for i in range(n):
    index_list.append(i)

# Make a list of the numbers from 0 to k-1
k_list = []
for i in range(k):
    k_list.append(i)

# Make a list of the numbers from 0 to n-k-1
n_k_list = []
for i in range(n-k):
    n_k_list.append(i)

# Reverse the string list
string_list.reverse()

# Make an empty list to store the new string
new_string_list = []

# Find the new string
for i in n_k_list:
    new_string_list.append(string_list[i])

# Reverse the new string list
new_string_list.reverse()

# Make a list to store the last k characters
last_k_list = []

# Find the last k characters
for i in k_list:
    last_k_list.append(string_list[i])

# Add the last k characters to the new string
for i in last_k_list:
    new_string_list.append(i)

# Make a new string
final_string = ""

for i in new_string_list:
    final_string += i

# Print the final string
print(final_string)
