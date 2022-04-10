
def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = [int(x) for x in input().split()]  # a is a list of integers
        a_count = dict()  # a_count is a dictionary
        for elem in a:  # elem is an element in a
            a_count[elem] = a_count.get(elem, 0) + 1  # a_count[elem] is the value of the key elem
        for elem in a:  # elem is an element in a
            if a_count[elem] >= 3:  # if the value of the key elem is greater than or equal to 3
                print("YES")  # print yes
                break  # break out of the loop
        else:  # if the for loop does not break
            print("NO")  # print no


if __name__ == '__main__':
    main()
