

def main():
    n = int(input())
    a = input().split()
    a = [int(x) for x in a]  # list comprehension
    a.sort()  # inplace sorting
    count = 0  # variable to store the difference
    for i in range(0, n, 2):  # looping through the list
        count += a[i+1] - a[i]  # calculating the difference
    print(count)  # printing the result


if __name__ == "__main__":
    main()
