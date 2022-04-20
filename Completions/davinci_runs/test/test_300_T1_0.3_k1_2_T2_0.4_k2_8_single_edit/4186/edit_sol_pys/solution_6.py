import sys

def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    #write your code here
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)


# n = int(input())
# a = list(map(int, input().split()))

# # Create a dictionary of skills and their counts
# skills = {}
# for i in a:
#     if i not in skills:
#         skills[i] = 1
#     else:
#         skills[i] += 1

# # Find the number of teams that can be formed
# num_teams = 0
# for i in skills:
#     num_teams += skills[i] // 2

# # Find the number of problems that need to be solved
# num_problems = 0
# for i in skills:
#     num_problems += skills[i] % 2

# # Print the answer
# print(num_problems + (n // 2) - num_teams)
