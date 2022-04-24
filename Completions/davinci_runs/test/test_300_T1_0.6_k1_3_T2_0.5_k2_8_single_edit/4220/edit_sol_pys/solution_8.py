
with open('input.txt') as f:
    k, s = f.readline(), f.readline()
    if int(k) > len(s):
        print(s)
    else:
        print(s[:int(k)] + '...')
