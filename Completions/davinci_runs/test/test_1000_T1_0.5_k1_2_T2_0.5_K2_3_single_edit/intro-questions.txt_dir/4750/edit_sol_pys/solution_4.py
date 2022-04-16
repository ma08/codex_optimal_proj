

def two_segments():
    q = int(input())
    for i in range(q):
        left_1, right_1, left_2, right_2 = map(int, input().split())
        if left_1 == right_1:
            print(left_1, left_2)
        elif left_2 == right_2:
            print(left_1, left_2)
        else:
            print(left_1, left_2 + 1)

two_segments()
