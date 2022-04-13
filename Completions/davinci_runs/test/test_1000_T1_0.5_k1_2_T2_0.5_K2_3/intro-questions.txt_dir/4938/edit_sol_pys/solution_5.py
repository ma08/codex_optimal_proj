

num_men = int(input())
num_women = int(input())
num_tables = int(input())
max_people = int(input())

print(min(num_men, num_women, num_tables * max_people))
