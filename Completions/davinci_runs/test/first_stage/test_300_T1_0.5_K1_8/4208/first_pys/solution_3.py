

n = int(input())
l = input()
r = input()

l_dict = {}
r_dict = {}

for i in range(n):
    if l[i] == "?":
        if "?" not in l_dict:
            l_dict["?"] = [i + 1]
        else:
            l_dict["?"].append(i + 1)
    else:
        if l[i] not in l_dict:
            l_dict[l[i]] = [i + 1]
        else:
            l_dict[l[i]].append(i + 1)

for i in range(n):
    if r[i] == "?":
        if "?" not in r_dict:
            r_dict["?"] = [i + 1]
        else:
            r_dict["?"].append(i + 1)
    else:
        if r[i] not in r_dict:
            r_dict[r[i]] = [i + 1]
        else:
            r_dict[r[i]].append(i + 1)

count = 0
for key in l_dict:
    if key in r_dict:
        count += min(len(l_dict[key]), len(r_dict[key]))
    elif "?" in r_dict:
        count += len(l_dict[key])

for key in r_dict:
    if key not in l_dict and key != "?":
        count += len(r_dict[key])

print(count)

for key in l_dict:
    if key in r_dict:
        for i in range(min(len(l_dict[key]), len(r_dict[key]))):
            print(str(l_dict[key][i]) + " " + str(r_dict[key][i]))
    elif "?" in r_dict:
        for i in range(len(l_dict[key])):
            print(str(l_dict[key][i]) + " " + str(r_dict["?"][i]))

for key in r_dict:
    if key not in l_dict and key != "?":
        for i in range(len(r_dict[key])):
            print(str(l_dict["?"][i]) + " " + str(r_dict[key][i]))