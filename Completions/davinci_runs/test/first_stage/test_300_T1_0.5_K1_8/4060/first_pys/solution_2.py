

n = int(input())
s = input()

if s.count("(") != s.count(")"):
    print(0)
    exit()

# count the number of open brackets
# for each close bracket, if there are open brackets, the bracket can be either open or close
# if there are no open brackets, it can only be open
# if there are more close brackets than open brackets, it can only be open

# count the number of close brackets
# for each open bracket, if there are close brackets, the bracket can be either open or close
# if there are no close brackets, it can only be close
# if there are more open brackets than close brackets, it can only be close

open_brackets = 0
close_brackets = 0

for c in s:
    if c == "(":
        open_brackets += 1
    elif c == ")":
        close_brackets += 1

open_count = 0
close_count = 0
for c in s:
    if c == "(":
        open_count += 1
    elif c == ")" and open_brackets > close_brackets:
        open_count += 1

for c in s:
    if c == ")" and open_brackets > close_brackets:
        close_count += 1
    elif c == ")":
        close_count += 1

print(open_count + close_count)