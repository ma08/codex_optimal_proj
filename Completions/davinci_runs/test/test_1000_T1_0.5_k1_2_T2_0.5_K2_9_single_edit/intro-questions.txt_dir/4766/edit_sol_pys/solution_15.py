
n = int(input())

for i in range(n):
    line = input()
    line_list = line.split()

    if len(line_list) > 2 and line_list[0] == "Simon" and line_list[1] == "says": # if the line is longer than 2 words, and the first 2 words are "Simon says"
        print(" ".join(line_list[2:]))
