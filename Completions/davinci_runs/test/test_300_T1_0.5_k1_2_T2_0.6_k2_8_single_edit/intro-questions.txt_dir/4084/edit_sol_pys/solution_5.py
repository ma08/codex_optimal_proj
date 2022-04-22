

n = int(input())

k = int(input())

m = int(input())

arr = []

x = n

while x > 0:

    arr.append(x)

    x = x - 1

if k > m:

    print("1")

else:

    if n == m:

        print("1")

    else:

        y = arr[0]

        while y <= m:

            y = y + k

            if y == m:

                print("1")

                break

            else:

                print("0")
