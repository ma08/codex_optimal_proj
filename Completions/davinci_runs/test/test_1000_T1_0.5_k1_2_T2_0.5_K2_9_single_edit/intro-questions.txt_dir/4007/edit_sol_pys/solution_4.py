

n = int(input())  # number of students
g = [int(x) for x in input().split()]  # gifts
s = [int(x) for x in input().split()]  # students

# Find students who don't know who to give gifts to
# and students who don't know who gives them gifts
no_gift_to = []  # students who don't know who to give gifts to
no_gift_from = []  # students who don't know who gives them gifts
for i in range(n):
    if g[i] == 0:
        no_gift_to.append(i)
    else:
        if g[g[i] - 1] == 0:
            no_gift_from.append(g[i] - 1)

# Give gifts to students who don't know who gives them gifts
for i in range(len(no_gift_to)):
    g[no_gift_from[i]] = no_gift_to[i] + 1

# Give gifts to students who don't know who to give gifts to
for i in range(len(no_gift_to)):
    g[no_gift_to[i]] = no_gift_from[i] + 1

# Find students who don't know who to give gifts to
# and students who don't know who gives them gifts
no_student_to = []  # students who don't know who to give gifts to
no_student_from = []  # students who don't know who gives them gifts
for i in range(n):
    if s[i] == 0:
        no_student_to.append(i)
    else:
        if s[s[i] - 1] == 0:
            no_student_from.append(s[i] - 1)

# Give gifts to students who don't know who gives them gifts
for i in range(len(no_student_to)):
    s[no_student_from[i]] = no_student_to[i] + 1

# Give gifts to students who don't know who to give gifts to
for i in range(len(no_student_to)):
    s[no_student_to[i]] = no_student_from[i] + 1

print(" ".join(str(x) for x in g))
print(" ".join(str(x) for x in s))
