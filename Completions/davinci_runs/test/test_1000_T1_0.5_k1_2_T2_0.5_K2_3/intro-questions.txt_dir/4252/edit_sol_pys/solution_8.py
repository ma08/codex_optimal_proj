
file_name = file_name.lower()
n = int(input())
file_name = input().lower()


count = 0

for i in range(2, n-1):  # iterate through all the letters except the first 2 and last 2
    if file_name[i-2] == 'x' and file_name[i-1] == 'x' and file_name[i] == 'x':  # if three x's in a row
        if file_name[i+1] == 'x' or file_name[i-3] == 'x':  # if the next letter or the previous letter is an x
            continue
        else:
            count += 1  # if it's not an x then add 1 to the count

print(count)
