

def main():
    # read data for n lines
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(input())

    # solve
    # solve
    # create a dictionary to store the number of occurences of each character
    d = {}
    for i in range(n):
        if arr[i] in d:
            d[arr[i]] += 1
        else:
            d[arr[i]] = 1
    for key in d:
        print(key, d[key])

main()
