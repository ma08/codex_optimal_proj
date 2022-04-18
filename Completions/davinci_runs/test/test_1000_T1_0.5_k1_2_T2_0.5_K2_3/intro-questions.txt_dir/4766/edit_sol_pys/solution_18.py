

n = int(input())

for i in range(n):
    line = input()
    line_list = line.split()


#fix spelling mistakes

    if len(line_list) >= 2 and line_list[0] == "Simon" and line_list[1] == "says":
        print(" ".join(line_list[2:]))
