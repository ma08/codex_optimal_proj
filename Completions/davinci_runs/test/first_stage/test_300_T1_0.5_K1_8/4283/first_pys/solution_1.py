

#----------------------------------------------------------------------------------

"""
    Approach:
    1. Sort the skills
    2. Iterate over the skills
        - If the difference between the current skill and the previous skill is less than 5, increment the count
        - Else, update the max_count
"""

def main():
    n = int(input())
    skills = list(map(int, input().split()))
    skills.sort()

    prev_skill = skills[0]
    count = 1
    max_count = 1

    for i in range(1, n):
        if skills[i] - prev_skill <= 5:
            count += 1
        else:
            max_count = max(max_count, count)
            count = 1
        prev_skill = skills[i]

    max_count = max(max_count, count)

    print(max_count)

if __name__ == '__main__':
    main()